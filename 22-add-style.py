import os
import sys
import re

# Inserts the style sheet link, generates relative path to the file
# based on the directory specified which is treated as the top level or web root

def process_html_file(file_path, relative_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Regex to find </title> tag
    title_regex = re.compile(r'</title>', re.IGNORECASE)
    match = title_regex.search(content)

    if match:
        # Insert the indented stylesheet link on a new line after </title> tag
        insert_index = match.end()
        stylesheet_link = f'\n  <link rel="stylesheet" href="{relative_path}styles.css">'
        modified_content = content[:insert_index] + stylesheet_link + content[insert_index:]

        # Write the modified content back to the file
        with open(file_path, 'w') as file:
            file.write(modified_content)
        print(f"Processed: {file_path}")

def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                # Calculate relative path for the stylesheet link
                relative_path = os.path.relpath(directory, root) + '/' if root != directory else ''
                process_html_file(file_path, relative_path)

if __name__ == "__main__":
    # Check if the directory argument is provided
    if len(sys.argv) != 2:
        print("Usage: python add_stylesheet.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]

    # Check if the provided directory exists
    if not os.path.isdir(directory):
        print(f"Error: Directory '{directory}' not found.")
        sys.exit(1)

    process_directory(directory)
