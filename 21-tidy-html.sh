#!/bin/bash
# HTML Tidy script
# Finds all HTML files from working dir specified down
# Handles two types of input charater encoding
# Outputs in us-ascii as this converts non-standard characters to HTML entities
# HTML Tidy optios set via config file

# Check if a directory is provided as a command-line argument
if [ $# -eq 0 ]; then
    echo "Usage: $0 <directory>"
    exit 1
fi

# Get the directory from the command line
directory=$1

# Check if the directory exists
if [ ! -d "$directory" ]; then
    echo "Directory not found: $directory"
    exit 1
fi

# Set the config file path in the current directory
config_file="./21-tidy-config.txt"

# Recursively find HTML files in the specified directory and run html-tidy on them
find "$directory" -type f -name "*.html" | while read -r file; do
    # Detect input file encoding
    encoding=$(file -b --mime-encoding "$file")

    # Determine the appropriate tidy option based on the detected encoding
    case $encoding in
        "iso-8859-1")
            tidy_option="-win1252"
            ;;
        "us-ascii")
            tidy_option="-ascii"
            ;;
        *)
            tidy_option=""
            ;;
    esac

    # Run html-tidy with the detected encoding option
    tidy -config "$config_file" $tidy_option -m "$file"

    echo "html-tidy run on: $file with encoding: $encoding"
done

echo "Done!"
