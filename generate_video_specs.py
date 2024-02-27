from generate_specs_template import MainPageSpecsGenerator


class VideoPageSpecsGenerator(MainPageSpecsGenerator):
    def addition_specs(self,photo_base) -> dict:
        return {
            "ytb_id": "",
        }


video_specs_generator = VideoPageSpecsGenerator("videography")


if __name__ == "__main__":
    video_specs_generator.generate_json_for_main_page()
