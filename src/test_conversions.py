import unittest
from conversions import text_node_to_html_node
from textnode import TextNode,TextType
from htmlnode import ParentNode, LeafNode
class TestConversion(unittest.TestCase):
    def test_tn_to_hn(self):
        node = TextNode("A picture of a penguin",TextType.image,"https://upload.wikimedia.org/wikipedia/commons/a/a3/Aptenodytes_forsteri_-Snow_Hill_Island%2C_Antarctica_-adults_and_juvenile-8.jpg")
        node2 = LeafNode("img","",{"src":"https://upload.wikimedia.org/wikipedia/commons/a/a3/Aptenodytes_forsteri_-Snow_Hill_Island%2C_Antarctica_-adults_and_juvenile-8.jpg","alt":"A picture of a penguin"})
        self.assertEqual(text_node_to_html_node(node).to_html(),node2.to_html())


