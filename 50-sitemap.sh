#!/bin/bash

# Generates a sitemap.xml file
# Directory passed as argument is treated as top level or web root
# sitemap.xml is written into that directory
# Note this will find all html files in the file structure
# regardless of if they are linked to in the website or not
# Note "path/to/index.html" is replaced with "path/to/" 
# as its assumed page links use the directory path with out index.html

# Check if a directory is provided as an argument
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <top-level-directory>"
    exit 1
fi

# Assign the provided directory to a variable
top_level_directory="$1"

# Specify the domain name of the site with out trailing /
domain="https://www.example.com"

# Full path for the sitemap.xml file in the top-level directory
sitemap_file="$top_level_directory/sitemap.xml"

# Create or overwrite the sitemap.xml file
echo '<?xml version="1.0" encoding="UTF-8"?>' > "$sitemap_file"
echo '<!-- sitemap-generator-url="https://github.com/lonney9/HTML-Scripts/blob/main/50-sitemap.sh" -->' >> "$sitemap_file"
echo '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' >> "$sitemap_file"

# Find all HTML files in the specified directory and subdirectories
find "$top_level_directory" -name '*.html' | while read -r file; do
    # Get the last modification date of the file in the correct format (UTC)
    modification_date=$(TZ=UTC stat -f "%Sm" -t "%Y-%m-%dT%H:%M:%SZ" "$file")

    # Extract the relative path from the top-level directory
    relative_path=${file#"$top_level_directory"}

    # Replace "/index.html" with "/" # we assume any html page links will use "/" and not "/index.html"
    relative_path=${relative_path//\/index.html/\/}

    # Print the URL and modification date to the sitemap.xml file
    echo "  <url>" >> "$sitemap_file"
    echo "    <loc>$domain$relative_path</loc>" >> "$sitemap_file"
    echo "    <lastmod>$modification_date</lastmod>" >> "$sitemap_file"
    echo "  </url>" >> "$sitemap_file"
done

# Close the urlset tag in sitemap.xml
echo '</urlset>' >> "$sitemap_file"

echo "Sitemap generated successfully at $sitemap_file"
