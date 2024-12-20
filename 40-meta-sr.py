import os
import re
import argparse

# Meta keywords search and repalce script
# Probably needs some refinement

def find_and_replace(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Find meta tag with name="keywords" and replace "VHF" with "VHF / UHF"
    new_content = re.sub(r'<meta\s+name="keywords"\s+content="[^"]*VHF[^"]*"', 
                         lambda match: match.group().replace('VHF', 'VHF / UHF'), content)

    # Update the file with the new content only if a replacement occurred
    if new_content != content:
        with open(file_path, 'w') as updated_file:
            updated_file.write(new_content)

def process_html_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                find_and_replace(file_path)
                print(f'Replaced keyword in {file_path}')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Recursively find and replace meta keyword in HTML files.')
    parser.add_argument('directory', help='Directory path to start the search.')

    args = parser.parse_args()

    process_html_files(args.directory)
