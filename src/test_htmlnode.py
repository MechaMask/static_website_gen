import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode
class TestHTMLNode(unittest.TestCase):
    def test_values(self):
        node = HTMLNode("p","Hello Everyone!")
        node2 = HTMLNode("p","Hello Everyone!", None, None)
        self.assertEqual(node.value,node2.value)
        self.assertEqual(node.tag,node2.tag)
        self.assertEqual(node.tag,"p")
        self.assertEqual(node.value,"Hello Everyone!")
        self.assertEqual(node.children,None)
        self.assertEqual(node.props,None)
    def test_props_to_html(self):
        node = HTMLNode("div","Hello Everyone!", None, {"class":"greeting","href":"https://boot.dev"})
        self.assertEqual(node.props_to_html()," class=\"greeting\" href=\"https://boot.dev\"")
    def test_repr(self):
        node = HTMLNode("p","Hello Everyone!")
        repr_text = "HTMLNode(p, Hello Everyone!, None, None)"
        self.assertEqual(repr(node),repr_text)
class TestLeafNode(unittest.TestCase):
        def test_notag(self):
            node = LeafNode(None,"This is raw text.",None)
            self.assertEqual(node.tag,None)
            self.assertEqual(node.value,"This is raw text.",None)
            self.assertEqual(node.props,None)
        def test_to_html(self):
            paragraph = LeafNode("p", "This is a very extensive paragraph that takes hours to finish reading...",None)
            clickme = LeafNode("a","Click me!", {"href":"https://www.google.com"})
            self.assertEqual(paragraph.to_html(),"<p>This is a very extensive paragraph that takes hours to finish reading...</p>")
            self.assertEqual(clickme.to_html(),"<a href=\"https://www.google.com\">Click me!</a>")
class TestParentNode(unittest.TestCase):
    def test_nested_parents(self):
        node = ParentNode("p",[ParentNode("b",[ParentNode("i",[LeafNode(None,"Leaf!!")])])])
        self.assertEqual(node.to_html(),"<p><b><i>Leaf!!</i></b></p>")
    def test_tohtml(self):
        node = ParentNode("p",
                [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
            ])
        self.assertEqual(node.to_html(),"<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")
    def test_complex_tree(self):
        tree = ParentNode("div",[ParentNode("p",[LeafNode(None,"Learn to code for free. freeCodeCamp's open source curriculum has helped more than 40,000 people get jobs as developers. "),LeafNode("a","Get started",{"href":"https://www.freecodecamp.org/learn/", "class":"cta-button", "id":"learn-to-code-cta","rel":"noopener noreferrer","target":"_blank"})])],{"class":"learn-cta-row" , "data-test-label":"learn-cta-row"})
        text = '<div class="learn-cta-row" data-test-label="learn-cta-row"><p>Learn to code for free. freeCodeCamp\'s open source curriculum has helped more than 40,000 people get jobs as developers. <a href="https://www.freecodecamp.org/learn/" class="cta-button" id="learn-to-code-cta" rel="noopener noreferrer" target="_blank">Get started</a></p></div>'
        self.assertEqual(tree.to_html(),text)
