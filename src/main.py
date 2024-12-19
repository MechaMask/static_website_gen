from textnode import TextNode, TextType
from htmlnode import LeafNode, ParentNode

def main():
    text1 = TextNode("This is a text node","bold","https://www.boot.dev")
    text2 = TextNode("This is a text node","bold","https://www.boot.dev")
    print(text1)
    print(text2)
    print(text1 == text2)
main()
