import os
import json


def generate_json_for_collections(photo_file_path):
    # Extract the photo name without extension and the extension
    music_name, photo_extension = os.path.splitext(os.path.basename(photo_file_path))

    # Create a dictionary with the photo's specifications
    music_specs = {
        'name': music_name,
        'description':'',
        'sc_id': "",
        'sc_name': music_name.lower().replace(' ','-'),
        "lyrics": f"https://raw.githubusercontent.com/hunthinniap/portfolio_asset/main/music/{music_name}/lyrics.txt",
        "Motivation": f"https://raw.githubusercontent.com/hunthinniap/portfolio_asset/main/music/{music_name}/motivation.txt"
    }
    # Create a directory with the name of the photo
    directory_name = f'music/{music_name}'
    os.makedirs(directory_name, exist_ok=True)

    # Define the path for the specs.json file inside the new directory
    json_file_path = os.path.join( directory_name, 'specs.json')

    # Write the photo specifications to the specs.json file
    if not os.path.exists(json_file_path):
        with open(json_file_path, 'w') as json_file:
            json.dump(music_specs, json_file, indent=4)
    lyrics_path = directory_name+'/lyrics.txt'
    if not os.path.exists(lyrics_path):
        with open(lyrics_path,'w') as f:
            pass
    motive_path = directory_name+'/motivation.txt'
    if not os.path.exists(motive_path):
        with open(motive_path,'w') as f:
            pass

photos_directory_path = 'music_cover'

# List all files in the directory
all_files = os.listdir(photos_directory_path)

# Filter for photo files with common image file extensions
photo_files = [file for file in all_files if file.lower().endswith(('.jpg', '.jpeg', '.png', ))]

# Iterate over the photo files and generate JSON for each
for photo_file in photo_files:
    photo_file_path = os.path.join(photos_directory_path, photo_file)
    generate_json_for_collections(photo_file_path)