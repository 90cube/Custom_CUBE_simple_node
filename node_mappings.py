# ComfyUI/custom_nodes/MyCustomNodes/node_mappings.py

from .nodes.CB_TestNode import CB_TestNode
from .nodes.CB_NodeButton import CB_NodeButton
from .nodes.CB_AdvancedResizer import CB_AdvancedResizer
from .nodes.CB_RatioResizer import CB_RatioResizer
from .nodes.CB_AdditionalPromptNodes import (
    CB_ArmPromptNode,
    CB_FacePromptNode,
    CB_FantasyArmorPromptNode,
    CB_HeadPromptNode,
    CB_FootPromptNode,
    CB_FullBodyPromptNode,
    CB_HandPromptNode,
    CB_UpperBodyPromptNode,
    CB_LegPromptNode,
    CB_LowerBodyPromptNode,
    CB_StylePromptNode,
    CB_SubItemPromptNode,
)

NODE_CLASS_MAPPINGS = {
    "CB_TestNode": CB_TestNode,
    "CB_NodeButton": CB_NodeButton,
    "CB_AdvancedResizer": CB_AdvancedResizer,
    "CB_RatioResizer": CB_RatioResizer,
    "CB_HeadPromptNode": CB_HeadPromptNode,
    "CB_StylePromptNode": CB_StylePromptNode,
    "CB_FullBodyPromptNode": CB_FullBodyPromptNode,
    "CB_UpperBodyPromptNode": CB_UpperBodyPromptNode,
    "CB_LowerBodyPromptNode": CB_LowerBodyPromptNode,
    "CB_LegPromptNode": CB_LegPromptNode,
    "CB_ArmPromptNode": CB_ArmPromptNode,
    "CB_HandPromptNode": CB_HandPromptNode,
    "CB_FootPromptNode": CB_FootPromptNode,
    "CB_FacePromptNode": CB_FacePromptNode,
    "CB_SubItemPromptNode": CB_SubItemPromptNode,
    "CB_FantasyArmorPromptNode": CB_FantasyArmorPromptNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CB_TestNode": "CB Test Node",
    "CB_NodeButton": "CB Node Button",
    "CB_AdvancedResizer": "CB Advanced Resizer",
    "CB_RatioResizer": "CB Ratio Resizer",
    "CB_HeadPromptNode": "CB Head Prompt",
    "CB_StylePromptNode": "CB Style Prompt",
    "CB_FullBodyPromptNode": "CB Full Body Prompt",
    "CB_UpperBodyPromptNode": "CB Upper Body Prompt",
    "CB_LowerBodyPromptNode": "CB Lower Body Prompt",
    "CB_LegPromptNode": "CB Leg Prompt",
    "CB_ArmPromptNode": "CB Arm Prompt",
    "CB_HandPromptNode": "CB Hand Prompt",
    "CB_FootPromptNode": "CB Foot Prompt",
    "CB_FacePromptNode": "CB Face Prompt",
    "CB_SubItemPromptNode": "CB Sub Item Prompt",
    "CB_FantasyArmorPromptNode": "CB Fantasy Armor Prompt",
}
