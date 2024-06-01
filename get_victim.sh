#!/bin/bash

# Path to the victim.list file
file_path="./victim.list"

# Check if the file exists
if [ ! -f "$file_path" ]; then
    echo "The victim.list file does not exist"
    exit 1
elif [ ! -s "$file_path" ]; then
    echo "The victim.list file is empty"
    exit 1
else
    cat "$file_path"
fi