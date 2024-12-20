import os
import re
import sys

# This was used to:
    # Remove all opening and closing font tags
    # Remove everything from the body tag (typically background, link colors etc)
    # Remove the bold tags from around the pre tags
    # Remove the doctype
        # HTML tidy seemed to trip up over it and produce HTML4 in some cases, with out it writes HTML5 doctype
    # Removed the alt element from the img tags, these only had the image name and size set
# HTML now ready to have HTML tidy run w/o CSS option

def remove_font_tags(file_path):
    with open(file_path, 'r', encoding='latin-1') as file:
        content = file.read()

    # Remove <font> tags and attributes (case-insensitive)
    content = re.sub(r'<\s*font[^>]*?>|<\s*/\s*font\s*>', '', content, flags=re.IGNORECASE)

    with open(file_path, 'w', encoding='latin-1') as file:
        file.write(content)

def clean_body_tags(file_path):
    with open(file_path, 'r', encoding='latin-1') as file:
        content = file.read()

    # Simplify <body> tags (case-insensitive)
    content = re.sub(r'<\s*body[^>]*?>', '<body>', content, flags=re.IGNORECASE)

    with open(file_path, 'w', encoding='latin-1') as file:
        file.write(content)

def clean_pre_tags(file_path):
    with open(file_path, 'r', encoding='latin-1') as file:
        content = file.read()

    # Replace <b><pre> or <pre><b> with <pre> (case-insensitive)
    content = re.sub(r'<\s*b\s*>\s*<\s*pre\s*>|<\s*pre\s*>\s*<\s*b\s*>', '<pre>', content, flags=re.IGNORECASE)

    # Replace </b></pre> or </pre></b> with </pre> (case-insensitive)
    content = re.sub(r'<\s*/\s*b\s*>\s*<\s*/\s*pre\s*>|<\s*/\s*pre\s*>\s*<\s*/\s*b\s*>', '</pre>', content, flags=re.IGNORECASE)

    with open(file_path, 'w', encoding='latin-1') as file:
        file.write(content)

def remove_doctype_lines(file_path):
    with open(file_path, 'r', encoding='latin-1') as file:
        lines = file.readlines()

    # Remove lines starting with "<!DOCTYPE HTML PUBLIC" (case-insensitive)
    lines = [line for line in lines if not re.match(r'^\s*<!DOCTYPE HTML PUBLIC', line, flags=re.IGNORECASE)]

    with open(file_path, 'w', encoding='latin-1') as file:
        file.writelines(lines)

def remove_alt_attribute(file_path):
    with open(file_path, 'r', encoding='latin-1') as file:
        content = file.read()

    # Remove alt attribute from <img> tags (case-insensitive)
    content = re.sub(r'<\s*img\b([^>]*)\s*alt\s*=\s*"[^"]*"\s*([^>]*)>', r'<img\1\2>', content, flags=re.IGNORECASE)

    with open(file_path, 'w', encoding='latin-1') as file:
        file.write(content)

def process_html_files(directory):
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            if file_name.lower().endswith('.html'):
                file_path = os.path.join(root, file_name)
                remove_font_tags(file_path)
                clean_body_tags(file_path)
                clean_pre_tags(file_path)
                remove_doctype_lines(file_path)
                remove_alt_attribute(file_path)
                print(f'Processed: {file_path}')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]

    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory.")
        sys.exit(1)

    process_html_files(directory)
