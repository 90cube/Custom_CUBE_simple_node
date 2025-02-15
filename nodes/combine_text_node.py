class CombineTextNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {},
            "optional": {"text": ("STRING",)},
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "combine_texts"
    CATEGORY = "Custom/Text"

    def combine_texts(self, **kwargs):
        texts = [value for key, value in kwargs.items()]
        combined_text = ", ".join(texts)
        return (combined_text,)
