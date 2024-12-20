import os
import re

# Reads meta keywords and writes a bookmarked topics.html index page
# Directory passed as commandline argument is treated as the top level or web root
# Use in conjunction with topic-footer.py

def build_topics_index(directory):
    index = {}

    def process_file(file_path):
        with open(file_path, 'r') as file:
            content = file.read()

            title_match = re.search(r'<title[^>]*>(.*?)<\/title>', content, re.IGNORECASE | re.DOTALL)
            keywords_match = re.search(r'<meta\s+name=["\']keywords["\']\s+content=["\'](.*?)["\']', content, re.IGNORECASE)

            if title_match and keywords_match:
                title = title_match.group(1).strip()
                keywords = keywords_match.group(1).strip()

                keyword_list = [keyword.strip() for keyword in keywords.split(',')]

                for keyword in keyword_list:
                    if keyword not in index:
                        index[keyword] = []

                    index[keyword].append({
                        'title': title,
                        'path': os.path.relpath(file_path, directory)
                    })

    def process_directory(directory_path):
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)

                if file.endswith('.html'):
                    process_file(file_path)

    process_directory(directory)
    return index

def generate_topics_index(directory):
    index = build_topics_index(directory)

    # Sort topics alphabetically
    sorted_topics = sorted(index.keys())

    with open(os.path.join(directory, 'topics.html'), 'w') as index_file:
        index_file.write('<!DOCTYPE html>\n<html lang="en">\n<head>\n <meta charset="UTF-8">\n <meta name="description" content="Cebik Website Topic Index">\n <meta name="generator" content="https://github.com/lonney9/HTML-Scripts/blob/main/30-topic-index.py">\n <title>Cebik Website Topic Index</title>\n <link rel="stylesheet" href="styles.css">\n</head>\n<body>\n')

        # Write page header
        index_file.write(' <h1 style="text-align: center; font-size: 2em;">Topic Index</h1>\n <img src="images/colorbar.gif" alt="hr" style="display: block; margin: auto;" width="540" height="4">\n')

        # Write "Jump To" unordered list
        index_file.write(' <br>\n  <ul style="column-count: 4;"><!-- https://stackoverflow.com/a/61698269 List column magic -->\n')
        for topic in sorted_topics:
            bookmark_name = re.sub(r'[^a-z0-9]+', '-', topic.lower())  # Modified line
            index_file.write(f'   <li><a href="#{bookmark_name}">{topic}</a></li>\n')
        index_file.write('  </ul>\n <br>\n <br>\n <img src="images/colorbar.gif" alt="hr" style="display: block; margin: auto;" width="540" height="4">\n')

        for topic in sorted_topics:
            bookmark_name = re.sub(r'[^a-z0-9]+', '-', topic.lower())  # Modified line
            index_file.write(f' <br>\n <p id="{bookmark_name}"></p>\n <h2>{topic}</h2>\n  <ul>\n')

            # Sort pages alphabetically under each topic
            sorted_pages = sorted(index[topic], key=lambda x: x['title'])
            for page_info in sorted_pages:
                index_file.write(f'   <li><a href="{page_info["path"]}">{page_info["title"]}</a></li>\n')

            index_file.write('  </ul>\n')

        index_file.write(' <br>\n <img src="images/colorbar.gif" alt="hr" style="display: block; margin: auto;" width="540" height="4">\n <br>\n</body>\n</html>')

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python script.py /path/to/website")
        sys.exit(1)

    website_directory = sys.argv[1]
    generate_topics_index(website_directory)
    print(" Index topics.html generated successfully.\n")
