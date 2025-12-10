from __future__ import annotations

from typing import List


class HeadPromptNode:
    """Build a headwear prompt from selectable options and free text."""

    wear_options: List[str] = ["hat", "helmet", "band", "crown", "cap", "hood"]
    color_options: List[str] = ["red", "blue", "yellow", "green", "black", "white", "gold", "silver"]
    above_options: List[str] = ["Angel ring", "Star", "Clouds", "Halo", "Moon", "Sun"]
    behind_options: List[str] = ["tails", "wings", "collars", "cape", "backpack", "aura"]

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "wear": (cls.wear_options, {"default": cls.wear_options[0]}),
                "color": (cls.color_options, {"default": cls.color_options[0]}),
                "above": (cls.above_options, {"default": cls.above_options[0]}),
                "behind": (cls.behind_options, {"default": cls.behind_options[0]}),
                "manual_input": (
                    "STRING",
                    {"default": "", "multiline": True, "placeholder": "Add additional prompt text"},
                ),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)
    FUNCTION = "build_prompt"
    CATEGORY = "utils/PromptEngineering"

    def build_prompt(self, wear: str, color: str, above: str, behind: str, manual_input: str):
        """Join the manual text with non-empty carousel selections."""

        parts = [
            value.strip()
            for value in [manual_input, wear, color, above, behind]
            if value is not None and value.strip()
        ]
        return (", ".join(parts),)
