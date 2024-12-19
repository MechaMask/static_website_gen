import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.bold)
        node2 = TextNode("This is a text node", TextType.bold)
        self.assertEqual(node,node2)
    def test_url(self):
        node = TextNode("http://localhost:8888",TextType.link,"http://localhost:8888")
        node2 = TextNode("http://localhost:8888",TextType.link,"http://localhost:8888")
        self.assertEqual(node,node2)
    def test_repr(self):
        node = TextNode("This is a text node", TextType.bold)
        repr_text = "TextNode(This is a text node, bold, None)"
        self.assertEqual(repr(node),repr_text)
    def test_url_neq(self):
        node = TextNode("http://localhost:8888",TextType.link,"http://localhost:8888")
        node2 = TextNode("http://localhost",TextType.link,"http://localhost:8888")
        self.assertNotEqual(node,node2)
    def test_url_mismatch(self):
        node = TextNode("http://localhost:8888",TextType.link,"http://localhost:8888")
        node2 = TextNode("http://localhost:8888",TextType.link,"http://localhost:8881")
        self.assertNotEqual(node,node2)
    def test_type(self):
        node = TextNode("Hello!",TextType.text)
        node2 = TextNode("Hello!",TextType.bold)
        self.assertNotEqual(node,node2)
    def test_none(self):
        node = TextNode("Hello!",TextType.text,None)
        node2 = TextNode("Hello!",TextType.text)
        self.assertEqual(node,node2)
    def test_enum(self):
        node = TextNode("Hello!",TextType.text,None)
        node2 = TextNode("Hello!","text")
        self.assertEqual(node,node2)


if __name__ == "__main__":
    unittest.main()

