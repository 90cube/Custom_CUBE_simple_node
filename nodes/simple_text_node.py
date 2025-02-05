from custom_nodes.base import NodeBase

class SimpleTextNode(NodeBase):
    def __init__(self):
        super().__init__()
        self.add_output("text", "STRING")  # 출력: 문자열

    def run(self):
        text = self.get_input_value("text", default="Hello, World!")
        self.set_output_value("text", text)

    def ui(self):
        self.add_input_text("text", label="Enter Text")  # 텍스트 입력 UI 추가
