import os
import json
from generate_specs_template import MainPageSpecsGenerator


class MusicPageSpecsGenerator(MainPageSpecsGenerator):
    def addition_specs(self,photo_base) -> dict:
        directory_name = f"{self.folder_path}/{photo_base}"
        os.makedirs(directory_name, exist_ok=True)
        lyrics_file_path = os.path.join(self.folder_path, f"{photo_base}/lyrics.txt")
        motivation_file_path = os.path.join(self.folder_path, f"{photo_base}/motivation.txt")
        if not os.path.exists(lyrics_file_path):
            with open(lyrics_file_path, "w") as file:
                pass  # Just create the file, no need to write anything
        if not os.path.exists(motivation_file_path):
            with open(motivation_file_path, "w") as file:
                pass
        return {"sc_id": ""
        }        


music_specs_generator = MusicPageSpecsGenerator("music")

def generate_json_for_collections(photo_file_path):
    # Extract the photo name without extension and the extension
    music_name, photo_extension = os.path.splitext(os.path.basename(photo_file_path))

    # Create a dictionary with the photo's specifications
    music_specs = {
        "name": music_name,
        "description": "",
        "sc_id": "",
        "sc_name": music_name.lower().replace(" ", "-"),
        "lyrics": f"https://raw.githubusercontent.com/hunthinniap/portfolio_asset/main/music/{music_name}/lyrics.txt",
        "motivation": f"https://raw.githubusercontent.com/hunthinniap/portfolio_asset/main/music/{music_name}/motivation.txt",
    }
    # Create a directory with the name of the photo
    directory_name = f"music/{music_name}"
    os.makedirs(directory_name, exist_ok=True)

    # Define the path for the specs.json file inside the new directory
    json_file_path = os.path.join(directory_name, "specs.json")

    # Write the photo specifications to the specs.json file
    if not os.path.exists(json_file_path):
        with open(json_file_path, "w") as json_file:
            json.dump(music_specs, json_file, indent=4)
    lyrics_path = directory_name + "/lyrics.txt"
    if not os.path.exists(lyrics_path):
        with open(lyrics_path, "w") as f:
            pass
    motive_path = directory_name + "/motivation.txt"
    if not os.path.exists(motive_path):
        with open(motive_path, "w") as f:
            pass



music_specs_generator = MusicPageSpecsGenerator('music')
music_specs_generator.generate_json_for_main_page()