# ComfyUI/custom_nodes/MyCustomNodes/node_mappings.py

from .nodes.CB_TestNode import CB_TestNode
from .nodes.CB_NodeButton import CB_NodeButton
from .nodes.CB_AdvancedResizer import CB_AdvancedResizer
from .nodes.CB_RatioResizer import CB_RatioResizer


NODE_CLASS_MAPPINGS = {
    "CB_TestNode": CB_TestNode,
    "CB_NodeButton": CB_NodeButton,
    "CB_AdvancedResizer": CB_AdvancedResizer,
    "CB_RatioResizer": CB_RatioResizer,

}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CB_TestNode": "CB Test Node",
    "CB_NodeButton": "CB Node Button",
    "CB_AdvancedResizer": "CB Advanced Resizer",
    "CB_RatioResizer": "CB Ratio Resizer",
}