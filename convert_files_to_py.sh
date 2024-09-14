#!/bin/bash
# Loop through all files in the directory except README.md
for file in *; do
    # Check if it's not a directory and doesn't end with .py or isn't README.md
    if [[ -f $file && $file != *.py && $file != "README.md" ]]; then
        mv "$file" "$file.py"
    fi
done
