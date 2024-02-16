import os
import json

def generate_json_for_collections(folder_path, base_url):
    json_file_path = os.path.join(folder_path, 'photos.json')
    photos_info = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                photo_url = os.path.join(base_url, folder_path, file).replace("\\", "/")
                photos_info.append({"src": photo_url, "alt": ""})

    with open(json_file_path, 'w') as json_file:
        json.dump(photos_info, json_file, indent=4)

def generate_json_for_cover(folder_path, base_url):
    json_file_path = os.path.join(folder_path, 'photos.json')
    photos_info = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                photo_url = os.path.join(base_url, folder_path, file).replace("\\", "/")
                photos_info.append({"cover_url": photo_url, "title": file[:-4], "link":f"/photography/{file[:-4]}"})

    with open(json_file_path, 'w') as json_file:
        json.dump(photos_info, json_file, indent=4)

base_url = 'https://raw.githubusercontent.com/hunthinniap/portfolio_asset/main/'
repo_path = 'Photography'  # Update this path

for folder in os.listdir(repo_path):
    folder_path = os.path.join(repo_path, folder)
    if os.path.isdir(folder_path):
        if folder != "cover_photos":       
            generate_json_for_collections(folder_path, base_url)
        else:
            generate_json_for_cover(folder_path,base_url)

generate_json_for_cover("music_cover",base_url)