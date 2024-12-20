import os
import sys
import re

def add_charset_to_html_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if <meta charset="UTF-8"> already exists
        if re.search(r'<meta\s+charset\s*=\s*["\']?UTF-8["\']?\s*/?>', content):
            print(f"Charset already exists in {file_path}. Skipping.")
            return

        # Add <meta charset="UTF-8"> under the <head> tag
        content = re.sub(r'(<head[^>]*>)', r'\1\n  <meta charset="UTF-8">', content, flags=re.IGNORECASE)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Charset added to {file_path}")

    except Exception as e:
        print(f"Error processing {file_path}: {e}")

def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.html'):
                file_path = os.path.join(root, file)
                add_charset_to_html_file(file_path)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory.")
        sys.exit(1)

    process_directory(directory)
