#!/bin/bash

# Activate the virtual environment
source env/bin/activate

# Prompt the user for directories
echo "Which directory would you like to scan for Markdown files?"
echo "Please enter a full or relative path."
read -e input1
echo "Which directory would you like the converted files & CSS to go to?"
echo "Please enter a full or relative path."
read -e input2

# Run the converter.py script
python converter.py "$input1" "$input2"