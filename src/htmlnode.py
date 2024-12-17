from textnode import TextNode
class HTMLNode():
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError("work in progress")
    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = []
        for attribute in self.props:
            props_html.append(f" {attribute}=\"{self.props[attribute]}\"")
        return "".join(props_html)
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self,tag,value,props=None):
        super().__init__(tag,value,None,props)
    def to_html(self):
        if self.value is None:
            raise ValueError("Invalid HTML: no value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self,tag,children,props=None):
        super().__init__(tag,None,children,props)
    def to_html(self):
        if self.tag is None:
            ValueError("Invalid HTML: no tag")
        if self.children is None:
            raise ValueError(f"Invalid ParentNode: children cant be {type(None)}")
        html_text = [f"<{self.tag}{self.props_to_html()}>"]
        for child in self.children:
            html_text.append(child.to_html())
        html_text.append(f"</{self.tag}>")
        return "".join(html_text)
