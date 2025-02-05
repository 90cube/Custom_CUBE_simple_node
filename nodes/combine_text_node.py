from custom_nodes.base import NodeBase

class CombineTextNode(NodeBase):
    def __init__(self):
        super().__init__()
        self.add_input("text_1", "STRING")
        self.add_input("text_2", "STRING")
        self.add_output("result", "STRING")

    def run(self):
        text1 = self.get_input_value("text_1", default="")
        text2 = self.get_input_value("text_2", default="")
        result = f"{text1} {text2}"  # 문자열 결합
        self.set_output_value("result", result)

    def ui(self):
        self.add_input_dropdown("delimiter", ["space", "comma", "newline"], label="Delimiter")
