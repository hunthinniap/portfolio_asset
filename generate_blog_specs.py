import os
import json
from generate_specs_template import MainPageSpecsGenerator


class BlogPageSpecsGenerator(MainPageSpecsGenerator):
    
    def addition_specs(self, photo_base) -> dict:
        txt_file_path = os.path.join(self.folder_path, f"{photo_base}.txt")
        if not os.path.exists(txt_file_path):
            with open(txt_file_path, "w") as file:
                pass  # Just create the file, no need to write anything
        return {
            "blog_link": f"https://raw.githubusercontent.com/hunthinniap/portfolio_asset/main/Blog/{photo_base}.txt",
            "blog_link": f"https://raw.githubusercontent.com/hunthinniap/portfolio_asset/main/Blog/{photo_base}.txt",
            "date": "",
        }


def generate_json_for_collections():
    # Extract the photo name without extension and the extension

    # Step 1: List all the photos in the "blog" folder.
    folder_path = "Blog"
    photos = [
        photo
        for photo in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, photo))
    ]

    # Step 2: For each photo, check if a corresponding .txt file exists. If it doesn't, create one.
    for photo in photos:
        txt_file_path = os.path.join(folder_path, f"{os.path.splitext(photo)[0]}.txt")
        if not os.path.exists(txt_file_path):
            with open(txt_file_path, "w") as file:
                pass  # Just create the file, no need to write anything

    # Step 3: Load the existing blog specs from a JSON file, or initialize an empty list if it doesn't exist.
    specs_file_path = "Blog/blog_specs.json"
    if os.path.exists(specs_file_path):
        with open(specs_file_path, "r") as file:
            blog_specs = json.load(file)
    else:
        blog_specs = []

    # Step 4: For each photo, check if its name exists in the blog specs. If not, append a new dictionary.
    for photo in photos:
        photo_base, _ = os.path.splitext(photo)
        if not any(spec["title"] == photo_base for spec in blog_specs):
            blog_specs.append(
                {
                    "title": photo_base,
                    "img_src": f"https://raw.githubusercontent.com/hunthinniap/portfolio_asset/main/Blog/{photo}",
                    "blog_link": f"https://raw.githubusercontent.com/hunthinniap/portfolio_asset/main/Blog/{photo_base}.txt",
                    "blog_link": f"https://raw.githubusercontent.com/hunthinniap/portfolio_asset/main/Blog/{photo_base}.txt",
                    "date": "",
                }
            )

    # Step 5: Save the updated blog specs back to the JSON file.
    with open(specs_file_path, "w") as file:
        json.dump(blog_specs, file, indent=4)


blog_page_generator = BlogPageSpecsGenerator("blog")


if __name__ == "__main__":
    blog_page_generator.generate_json_for_main_page()

