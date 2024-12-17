from htmlnode import LeafNode, ParentNode
from textnode import TextType, TextNode

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.default_text:
            return LeafNode(None,text_node.text)
        case TextType.bold_text:
            return LeafNode("b",text_node.text)
        case TextType.italic_text:
            return LeafNode("i",text_node.text)
        case TextType.code_text: 
            return LeafNode("code",text_node.text)
        case TextType.link:
            return LeafNode("a",text_node.text,{"href":text_node.url})
        case TextType.image:
            return LeafNode("img","",{"src":text_node.url,"alt":text_node.text})
        case _:
            raise Exception("Invalid TextNode")


