#!/bin/bash

# Check if the user provided a new string as an argument
if [ -z "$1" ]; then
  echo "Please provide a replacement string."
  exit 1
fi

# Define the list of files you want to process
FILES=("manage.py" "file2.txt" "file3.txt")  # Modify this list with your actual file names

# Loop through each file and replace 'boilerplate' with the new string
for FILE in "${FILES[@]}"; do
  if [ -f "$FILE" ]; then
    # Use sed to replace 'boilerplate' with the given argument
    sed -i '' "s/boilerplate/$1/g" manage.py
    echo "Replaced 'boilerplate' with '$1' in $FILE."
  else
    echo "File $FILE not found."
  fi
done
