# ComfyUI/custom_nodes/MyCustomNodes/node_mappings.py

from .nodes.CB_TestNode import CB_TestNode

NODE_CLASS_MAPPINGS = {
    "CB_TestNode": CB_TestNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CB_TestNode": "CB Test Node",
}