import os
import json


def generate_json_for_collections():
    # Extract the photo name without extension and the extension


    # Step 1: List all the photos in the "blog" folder.
    folder_path = "videography"
    photos = [photo for photo in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, photo))]

    specs_file_path = "videography/specs.json"
    if os.path.exists(specs_file_path):
        with open(specs_file_path, 'r') as file:
            specs = json.load(file)
    else:
        specs = []

    # Step 4: For each photo, check if its name exists in the blog specs. If not, append a new dictionary.
    for photo in photos:
        photo_base, _ = os.path.splitext(photo)
        if not any(spec['title'] == photo_base for spec in specs):
            specs.append({
                "img_src": f"https://raw.githubusercontent.com/hunthinniap/portfolio_asset/main/videography/{photo}",
                "title": photo_base,
                "description":"",
                "ytb_id":"",
            })

    # Step 5: Save the updated blog specs back to the JSON file.
    with open(specs_file_path, 'w') as file:
        json.dump(specs, file, indent=4)

if __name__ == '__main__':
    generate_json_for_collections()
