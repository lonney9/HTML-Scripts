import os
import re
import sys

# Replace the html tag with <html lang="en">
# Helps screen readers, in-borwser lang translation, SEO

def update_html_lang(directory):
    # Iterate through all files in the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                update_html_tag(file_path)

def update_html_tag(file_path):
    # Read the content of the HTML file
    with open(file_path, 'r') as file:
        content = file.read()

    # Update the entire <html> tag with <html lang="en">
    updated_content = re.sub(r'<html\b[^>]*>', r'<html lang="en">', content)

    # Write the updated content back to the file
    with open(file_path, 'w') as file:
        file.write(updated_content)

if __name__ == "__main__":
    # Check if a directory name is provided as an argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]

    # Check if the directory exists
    if not os.path.exists(directory):
        print(f"Directory '{directory}' not found.")
        sys.exit(1)

    # Update HTML files in the specified directory
    update_html_lang(directory)

    print("HTML tags updated successfully.")
