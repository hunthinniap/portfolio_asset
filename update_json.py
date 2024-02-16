import os
import json

def generate_json_for_folder(folder_path, base_url):
    json_file_path = os.path.join(folder_path, 'photos.json')
    photos_info = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                photo_url = os.path.join(base_url, os.path.relpath(root, folder_path), file).replace("\\", "/")
                photos_info.append({"url": photo_url})

    with open(json_file_path, 'w') as json_file:
        json.dump(photos_info, json_file, indent=4)

base_url = 'https://github.com/hunthinniap/portfolio_asset'
repo_path = '/photogrpahy'  # Update this path

for folder in os.listdir(repo_path):
    folder_path = os.path.join(repo_path, folder)
    if os.path.isdir(folder_path):
        generate_json_for_folder(folder_path, base_url)
