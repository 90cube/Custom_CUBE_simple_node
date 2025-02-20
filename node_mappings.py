# ComfyUI/custom_nodes/MyCustomNodes/node_mappings.py

from .nodes.CB_TestNode import CB_TestNode

NODE_CLASS_MAPPINGS = {
    "CB_TestNode": CB_TestNode,
    "CB_NodeButton": CB_NodeButton,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CB_TestNode": "CB Test Node",
    "CB_NodeButton": "CB Node Button",
}