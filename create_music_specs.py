import os
import json

photo_file_path = 'music_cover/Dusklight.jpg'

def generate_json_for_collections(photo_file_path):
    # Extract the photo name without extension and the extension
    photo_name, photo_extension = os.path.splitext(os.path.basename(photo_file_path))

    # Create a dictionary with the photo's specifications
    photo_specs = {
        'name': photo_name,
        'description':'',
        'sc_id': "",
        'sc_name': photo_name.lower().replace(' ','-'),
        "lyrics": "",
        "Motivation": ""
    }
    # Create a directory with the name of the photo
    directory_name = f'music/{photo_name}'
    os.makedirs(directory_name, exist_ok=True)

    # Define the path for the specs.json file inside the new directory
    json_file_path = os.path.join( directory_name, 'specs.json')

    # Write the photo specifications to the specs.json file
    with open(json_file_path, 'w') as json_file:
        json.dump(photo_specs, json_file, indent=4)

photos_directory_path = 'music_cover'

# List all files in the directory
all_files = os.listdir(photos_directory_path)

# Filter for photo files with common image file extensions
photo_files = [file for file in all_files if file.lower().endswith(('.jpg', '.jpeg', '.png', ))]

# Iterate over the photo files and generate JSON for each
for photo_file in photo_files:
    photo_file_path = os.path.join(photos_directory_path, photo_file)
    generate_json_for_collections(photo_file_path)