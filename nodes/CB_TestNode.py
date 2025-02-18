# ComfyUI/custom_nodes/MyCustomNodes/nodes/CB_TestNode.py

class CB_TestNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {},
            "optional": {}
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("test",)
    FUNCTION = "test_function"
    CATEGORY = "TEST/TEXT"

    def test_function(self):
        return ("TEST",)