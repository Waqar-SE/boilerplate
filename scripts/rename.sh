#!/bin/bash

# Check if the user provided a new string as an argument
if [ -z "$1" ]; then
  echo -e "\033[031;1mPlease provide a replacement string.\033[0m"
  exit 1
elif [ -d "./src/$1" ]; then
  echo -e "\033[031;1mDirectory '$1' already exists.\nplease select another name or remove existing directory if empty\033[0m"
  exit 1
fi

OLD_NAME="${2:-boilerplate}"
echo -e "\033[032m\nRenaming '$OLD_NAME' to '$1'......\n\033[0m"

# Define the list of files you want to process
FILES=("manage.py" "src/$OLD_NAME/settings.py" "src/$OLD_NAME/asgi.py" "src/$OLD_NAME/wsgi.py" "package.json" "pyproject.toml")  # Modify this list with your actual file names
RENAME_DIR=false

# Loop through each file and replace 'boilerplate' with the new string


for FILE in "${FILES[@]}"; do
  if [ -f "$FILE" ]; then
    if [ "$(grep -i -o "$OLD_NAME" "$FILE" | wc -l)" -gt 0 ]; then
      RENAME_DIR=true
    # Use sed to replace 'boilerplate' with the given argument
      sed -i '' "s/$OLD_NAME/$1/Ig" $FILE
      echo "Replaced "$OLD_NAME" with '$1' in $FILE."
    else
      echo "No match found in '$FILE'"
    fi
  else
    echo "File $FILE not found."
  fi
done

if [ "$RENAME_DIR" = true ]; then
  echo 'Renaming Project directory'
  cd "src"
  mv "$OLD_NAME" "$1"
fi

echo -e "\033[032m\nRename complete\033[0m"
