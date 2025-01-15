from htmlnode import LeafNode, ParentNode
from textnode import TextType, TextNode
import re

def extract_markdown_images(text):
    images = re.findall(r"\!\[(.*?)\]\((.*?)\)",text)
    return images

def extract_markdown_links(text):
    links = re.findall(r"(?<!\!)\[(.*?)\]\((.*?)\)",text)
    return links
def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.text:
            return LeafNode(None,text_node.text)
        case TextType.bold:
            return LeafNode("b",text_node.text)
        case TextType.italic:
            return LeafNode("i",text_node.text)
        case TextType.code: 
            return LeafNode("code",text_node.text)
        case TextType.link:
            return LeafNode("a",text_node.text,{"href":text_node.url})
        case TextType.image:
            return LeafNode("img","",{"src":text_node.url,"alt":text_node.text})
        case _:
            raise Exception("Invalid TextNode")
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.text:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_delimiter_old(old_nodes, delimiter, text_type):
    new_nodes= []
    for node in old_nodes:
        if node.text_type != TextType.text:
            new_nodes.append(node)
        elif ((text_type == TextType.code and delimiter != "`") or (text_type == TextType.bold and delimiter != "**") or (text_type == TextType.italic and delimiter != "*")):
            raise Exception(f"mismatching TextType \'{TextType.value}\' and delimiter \'{delimiter}\'")
        else:
            filtered_text = node.text.replace("**","") if text_type == TextType.italic else node.text 
            if filtered_text.count(delimiter) % 2 != 0:
                raise ValueError("Invalid markdown, formatted section not closed")
            print(filtered_text)
            l=0
            r=1
            last_block = 0
            element = ""
            del_length = len(delimiter)
            sections = []
            while r < len(filtered_text)-1:
                if filtered_text[l:l+del_length] == delimiter:
                    if filtered_text[r:r+del_length] == delimiter:
                        element = filtered_text[l+del_length:r]
                        print(element)
                        if element != "" and l != 0:
                            print(filtered_text[last_block:l])
                            sections.extend([
                                TextNode(filtered_text[last_block:l],TextType.text),
                                TextNode(element,text_type)])
                        else:
                            sections.append(TextNode(element,text_type))
                        last_block=r+del_length
                        l=last_block
                        r = l+1
                    else:
                        r+=1
                else:
                    l+=1
                    r+=1
            if last_block < len(filtered_text):
                print(filtered_text[last_block:])
                sections.append(TextNode(filtered_text[last_block:],TextType.text))
            new_nodes.extend(sections)
    return new_nodes
                



