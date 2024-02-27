import os
import json
from generate_specs_template import MainPageSpecsGenerator

class PhotoSpecsGenerator(MainPageSpecsGenerator):
    def addition_specs(self,photo_base) -> dict:
        folder_path = f"{self.folder_path}/{photo_base}"

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
            collection_photo_base, _ = os.path.splitext(photo)
            if not any(spec["title"] == collection_photo_base for spec in specs):
                basic_specs = {
                    "title": collection_photo_base,
                    "description":""
                }
                specs.append(basic_specs)

        # Step 5: Save the updated blog specs back to the JSON file.
        with open(specs_file_path, "w") as file:
            json.dump(specs, file, indent=4)

        return {}

photo_specs_generator = PhotoSpecsGenerator("photography")
photo_specs_generator.generate_json_for_main_page()
