#!/bin/bash
# Wrapper script for image-dedup.py script
# Cycles through the list of images
# Updates path to image
# Moves image to temp dir outside of working dir
# Deletes every instance of the image
# Moves image into the new images directory
# Moving preserves the original creation date of the file
# Update the hardcoded paths as needed..

mkdir path/to/web_root/images

# List of images, one per line
IMG_LIST="image1.gif
image2.gif
image3.jpg"

# Loop through each image in the list
while IFS= read -r IMAGE; do
    # Replace "image-dedup.py" with your actual script name
    python3 23-image-dedup.py path/to/web_root "$IMAGE"
    
    # Move the processed image to the specified directory
    mv "path/to/web_root/$IMAGE" images/
    
    # Find and delete the original image in the "content" directory
    find path/to/web_root -name "$IMAGE" -print -delete
    
    # Move the processed image to the "content/images" directory
    mv "images/$IMAGE" "path/to/web_root/images/"
done <<< "$IMG_LIST"

