import os
import re
import sys

# Update the first h2 tag to h1 for SEO
# CSS restyles the h1 to h2 since the default h1 text is too large

def update_h2_to_h1(html_file):
    with open(html_file, 'r') as file:
        content = file.read()

    # Use regular expressions to find the first occurrence of <h1>...</h1> or <h2>...</h2>
    h1_match = re.search(r'<h1>(.*?)</h1>', content, re.DOTALL)
    h2_match = re.search(r'<h2>(.*?)</h2>', content, re.DOTALL)

    if h1_match:
        print(f'The first heading tag is already <h1> in {html_file}. No changes needed.')
    elif h2_match:
        # Replace <h2>...</h2> with <h1>...</h1>
        updated_content = content[:h2_match.start()] + '<h1>' + h2_match.group(1) + '</h1>' + content[h2_match.end():]

        # Write the updated content back to the file
        with open(html_file, 'w') as file:
            file.write(updated_content)
        print(f'Updated the first <h2> tag to <h1> in {html_file}')
    else:
        print(f'No <h1> or <h2> tag found in {html_file}')

def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                html_file = os.path.join(root, file)
                update_h2_to_h1(html_file)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory>")
    else:
        directory = sys.argv[1]
        process_directory(directory)
