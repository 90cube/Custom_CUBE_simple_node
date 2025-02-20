import json
import os

class CB_NodeButton:
    BASE_DIR = os.path.join(os.path.dirname(__file__), "..", "nodebutton")

    def __init__(self):
        self.buttons = {}
        self.ensure_json_folder_exists()
        self.load_buttons_from_json()

    def ensure_json_folder_exists(self):
        if not os.path.exists(self.BASE_DIR):
            os.makedirs(self.BASE_DIR)

    def load_buttons_from_json(self, filename="comfyui_buttons.json"):
        file_path = os.path.join(self.BASE_DIR, filename)
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                data = json.load(f)
                for title, prompts in data.get("buttons", {}).items():
                    self.buttons[title] = (prompts, False)

    def save_buttons_to_json(self, filename="comfyui_buttons.json"):
        file_path = os.path.join(self.BASE_DIR, filename)
        data = {"buttons": {title: prompts for title, (prompts, _) in self.buttons.items()}}
        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "load_from_json": ("STRING", {"default": "comfyui_buttons.json"}),
                "save_to_json": ("STRING", {"default": ""}),
            },
            "optional": {
                "add_prompt": ("STRING", {"default": ""}),
                "button_label": ("STRING", {"default": ""}),
                "toggle_button": ("STRING", {"default": ""}),
                "save_to_json_button": ("BUTTON", {"label": "Save to JSON"}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("output_prompt",)
    FUNCTION = "process_node"
    CATEGORY = "90cube"

    def process_node(self, load_from_json, save_to_json, add_prompt="", button_label="", 
                     toggle_button="", save_to_json_button=False):

        self.load_buttons_from_json(load_from_json)

        if add_prompt and button_label:
            self.buttons[button_label] = (add_prompt.split(", "), False)

        if toggle_button in self.buttons:
            prompt, state = self.buttons[toggle_button]
            self.buttons[toggle_button] = (prompt, not state)

        if save_to_json_button and save_to_json:
            self.save_buttons_to_json(save_to_json)

        active_prompts = [prompt for prompt, state in self.buttons.values() if state]
        return (", ".join(active_prompts),)