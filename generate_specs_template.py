import os
import json


class MainPageSpecsGenerator:
    def __init__(self, folder_path) -> None:
        self.folder_path = folder_path

    def addition_specs(self,photo_base) -> dict:
        return {}

    def generate_json_for_main_page(self) -> None:
        # Extract the photo name without extension and the extension

        # Step 1: List all the photos in the "blog" folder.
        folder_path = self.folder_path
        photos = [
            photo
            for photo in os.listdir(folder_path)
            if os.path.isfile(os.path.join(folder_path, photo))
        ]

        specs_file_path = f"{folder_path}/specs.json"
        if os.path.exists(specs_file_path):
            with open(specs_file_path, "r") as file:
                specs = json.load(file)
        else:
            specs = []

        # Step 4: For each photo, check if its name exists in the blog specs. If not, append a new dictionary.
        for photo in photos:
            photo_base, _ = os.path.splitext(photo)
            if not any(spec["title"] == photo_base for spec in specs):
                basic_specs = {
                    "title": photo_base,
                    "description":""
                }
                basic_specs.update(self.addition_specs(photo_base))
                specs.append(basic_specs)

        # Step 5: Save the updated blog specs back to the JSON file.
        with open(specs_file_path, "w") as file:
            json.dump(specs, file, indent=4)
