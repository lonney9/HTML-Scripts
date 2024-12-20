import os
import argparse
import re

# Reads meta keywords and writes a linked bookmarked footer
# Directory passed as commandline argument is treated as the top level or web root
# Use in conjunction with topic-index.py

def find_html_files(directory):
    html_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                html_files.append(os.path.join(root, file))
    return html_files

def update_footer(html_file, topics, top_level_directory):
    with open(html_file, 'r') as file:
        html_content = file.read()

    footer_content = '  <p class="topics-footer">Topics: {}</p><br>'.format(", ".join(["<a href='{}'>{}</a>".format(os.path.relpath(os.path.join(top_level_directory, 'topics.html') + '#' + re.sub(r'[^a-z0-9]+', '-', topic.lower()), start=os.path.dirname(html_file)), topic) for topic in sorted(topics)]))

    # Check if an existing footer is present
    existing_footer_pattern = re.compile(r'  <p class="topics-footer">.*?</p><br>', re.DOTALL)
    if existing_footer_pattern.search(html_content):
        html_content = existing_footer_pattern.sub(footer_content, html_content)
    else:
        # If no existing footer, add the new footer on its own line above </body>
        html_content = html_content.replace('</body>', f'{footer_content}\n</body>', 1)

    with open(html_file, 'w') as file:
        file.write(html_content)

def process_html_files(top_level_directory):
    html_files = find_html_files(top_level_directory)

    for html_file in html_files:
        with open(html_file, 'r') as file:
            content = file.read()

        meta_keywords_match = re.search(r'<meta\s+name="keywords"\s+content="([^"]*)"\s*>', content)

        if meta_keywords_match:
            keywords_content = meta_keywords_match.group(1)
            topics = [topic.strip() for topic in keywords_content.split(',')]

            if topics:
                update_footer(html_file, topics, top_level_directory)

def main():
    parser = argparse.ArgumentParser(description='Add topics to HTML files based on meta keywords')
    parser.add_argument('directory', help='Top level directory containing HTML files')

    args = parser.parse_args()
    top_level_directory = args.directory

    process_html_files(top_level_directory)
    print(" Footers added successfully. \n")

if __name__ == '__main__':
    main()
