from enum import Enum

from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    LINK = "link"
    IMAGE = "image"
    CODE = "code"
    ITALIC = "italic"
    BOLD = "bold"

class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str = None):
        self.text = text
        self.text_type = text_type
        self.url = url
        
    def __eq__(self, other):
        if (self.text == other.text) and (self.text_type == other.text_type) and (self.url == other.url):
                return True
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
                
def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(value=text_node.text, tag=None)
        case TextType.LINK:
            return LeafNode(value=text_node.text, tag="a", props={"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode(value=text_node.text, tag="img", props={"src": text_node.url, "alt": text_node.text})
        case TextType.CODE:
            return LeafNode(value=text_node.text, tag="code")
        case TextType.ITALIC:
            return LeafNode(value=text_node.text, tag="i")
        case TextType.BOLD:
            return LeafNode(value=text_node.text, tag="b")
        case _:
            raise Exception(f"Invalid text type: {text_node.text_type}")
        
