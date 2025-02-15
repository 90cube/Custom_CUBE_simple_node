# __init__.py

from .nodes.combine_text_node import CombineTextNode
from .nodes.simple_text_node import SimpleTextNode
from .nodes.wildcard_category_node import WildcardCategoryNode

def register_custom_nodes():
    return [
        CombineTextNode(),
        SimpleTextNode(),
        WildcardCategoryNode(),
	CustomCubeSimpleNode()
    ]

NODE_CLASS_MAPPINGS = {
    "CombineTextNode": CombineTextNode,
    "SimpleTextNode": SimpleTextNode,
    "WildcardCategoryNode": WildcardCategoryNode,
    "CustomCubeSimpleNode": CustomCubeSimpleNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CombineTextNode": "Combine Text Node",
    "SimpleTextNode": "Simple Text Node",
    "WildcardCategoryNode": "🟦 Wildcard Selector",
    "CustomCubeSimpleNode": "Custom Cube Simple Node"
}
