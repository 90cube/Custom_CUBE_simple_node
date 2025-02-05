from .simple_text_node import SimpleTextNode
from .combine_text_node import CombineTextNode

def register_custom_nodes():
    return [
        SimpleTextNode(),
        CombineTextNode(),
    ]
