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
            "date": "",
        }



blog_page_generator = BlogPageSpecsGenerator("blog")


if __name__ == "__main__":
    blog_page_generator.generate_json_for_main_page()

