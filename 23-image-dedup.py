import os
import sys
import re

# De-duplicates images
# Specify dir as top level or web root, and the image name
# The relative path to that image will be re-written with the dir name 
# specified in images_directory

def update_image_links(file_path, directory, image_filename):
    # Specify the directory name at the top level
    images_directory = "images"

    # Calculate the new relative path to the images directory
    updated_img_src = os.path.relpath(
        os.path.join(directory, images_directory, image_filename),
        os.path.dirname(file_path)
    ).replace("\\", "/")

    with open(file_path, 'r') as file:
        content = file.read()

    # Regular expression to find all image tags
    img_tag_pattern = re.compile(r'<img[^>]*?>', re.IGNORECASE)

    # Find all image tags in the content
    img_tags = img_tag_pattern.findall(content)

    # Iterate through the found image tags
    for img_tag in img_tags:
        # Check if the specified image filename is present in the image tag
        if image_filename in img_tag:
            # Update the 'src' attribute of the matching image tag
            img_tag_updated = re.sub(r'src=[\'"](.*?{0}.*?)[\'"]'.format(re.escape(image_filename)), 'src="{0}"'.format(updated_img_src), img_tag, flags=re.IGNORECASE)

            # Replace the original image tag with the updated one
            content = content.replace(img_tag, img_tag_updated)

    # Write the updated content back to the HTML file
    with open(file_path, 'w') as file:
        file.write(content)

def process_html_files(directory, image_filename):
    # Get the absolute path of the directory
    directory = os.path.abspath(directory)

    # Iterate through all files in the directory and its subdirectories
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)

            # Check if the file is an HTML file
            if file_path.endswith(".html"):
                update_image_links(file_path, directory, image_filename)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <directory> <image_filename>")
        sys.exit(1)

    directory_name = sys.argv[1]
    image_filename = sys.argv[2]

    process_html_files(directory_name, image_filename)
    print("Image links updated successfully.")
