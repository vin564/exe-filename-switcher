# exe-filename-switcher

## Description

This repository contains a Python script for managing and renaming `.exe` files in a directory automatically. The script allows you to:

- Map `.exe` files to SHA-256 hashes and associate custom names with them.
- Rename a main `.exe` file based on your choice and rename the existing main file to a new name based on its hash.
- Ignore non-`.exe` files, ensuring that only relevant files are processed.

## Features

- **Hash Mapping**: Associate SHA-256 hashes of `.exe` files with custom names.
- **Automatic Renaming**: Replace the main `.exe` file with another and rename the current main file based on its hash.
- **Ease of Use**: Configure the name of the main `.exe` file as a variable, making it adaptable to various use cases.

## How to Use

1. **Copy the Script**: Place the script in the directory where your `.exe` files are located.
2. **Edit the `main_exe_name` Variable**: Update this variable in the script to the name of the `.exe` file you want to manage.
3. **Run the Script**: Execute the script with Python to perform the mapping and renaming:
   ```bash
   python script_name.py

## Requirements
- Python 3.x
- hashlib library (included in the standard Python library)
- json library (included in the standard Python library)
