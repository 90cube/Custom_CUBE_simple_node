from .wildcards import CLIPTextEncodeWithWildcards

class WildcardCategoryNode:
    def __init__(self):
        self.wc_manager = CLIPTextEncodeWithWildcards()

    def INPUT_TYPES(self):
        categories = self.wc_manager.get_available_categories()
        files = self.wc_manager.get_files_in_category(categories[0]) if categories else []

        return {
            "required": {
                "category": ("STRING", {"choices": categories}),
                "file": ("STRING", {"choices": files}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff})
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "process"

    CATEGORY = "CUBE Wildcards"

    def process(self, category, file, seed):
        return (self.wc_manager.read_wildcard(category, file, seed),)

def register_custom_nodes():
    return [
        WildcardCategoryNode(),  # 🚀 폴더별 와일드카드 선택 노드 추가!
    ]

NODE_CLASS_MAPPINGS = {
    "WildcardCategoryNode": WildcardCategoryNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "WildcardCategoryNode": "🟦 Wildcard Selector"
}
