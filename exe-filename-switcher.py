import os
import hashlib
import json

# Name of the main .exe file to be managed (replace with the desired name)
main_exe_name = 'filename.exe'  # Edit here to the desired name

# Current directory path
dir_path = os.path.dirname(os.path.realpath(__file__))
config_file = os.path.join(dir_path, 'file_map.json')

# Load hash-to-name mapping
if os.path.exists(config_file):
    with open(config_file, 'r') as f:
        hash_name_map = json.load(f)
else:
    hash_name_map = {}

# Function to calculate the SHA-256 hash of a file
def calculate_hash(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

# Map the hash of the main .exe file if it exists
current_file_path = os.path.join(dir_path, main_exe_name)
if os.path.exists(current_file_path):
    current_hash = calculate_hash(current_file_path)
    if current_hash not in hash_name_map:
        name = input(f'Enter a name for the hash of {main_exe_name} ({current_hash}): ')
        hash_name_map[current_hash] = name
        with open(config_file, 'w') as f:
            json.dump(hash_name_map, f, indent=4)

# List .exe files in the directory (excluding the main file and file_map.json)
files = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f)) and f.endswith('.exe') and f != main_exe_name]

# Map .exe files to hashes
file_hashes = {}
for file in files:
    file_path = os.path.join(dir_path, file)
    file_hash = calculate_hash(file_path)
    file_hashes[file] = file_hash
    if file_hash not in hash_name_map:
        name = input(f'Enter a name for the hash {file_hash} associated with {file}: ')
        hash_name_map[file_hash] = name

# Save updated mapping
with open(config_file, 'w') as f:
    json.dump(hash_name_map, f, indent=4)

# Show selection list of files
print(f"\nSelect the file to be renamed to {main_exe_name}:")
for i, file in enumerate(files, 1):
    print(f"{i} - {file}")

choice = int(input("Enter the number of the file: ")) - 1
selected_file = files[choice]
selected_file_path = os.path.join(dir_path, selected_file)
selected_file_hash = file_hashes[selected_file]

# Rename the current main .exe file if it exists
if os.path.exists(current_file_path):
    if current_hash in hash_name_map:
        new_name = f'{os.path.splitext(main_exe_name)[0]} ({hash_name_map[current_hash]}).exe'
        os.rename(current_file_path, os.path.join(dir_path, new_name))

# Rename the selected file to the main .exe name
os.rename(selected_file_path, current_file_path)
print(f"The file has been successfully renamed to {main_exe_name}.")
