import unittest
from conversions import * 
from textnode import TextNode,TextType
from htmlnode import ParentNode, LeafNode

class TestExtract(unittest.TestCase):
    def test_extract_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        images = extract_markdown_images(text)
        self.assertEqual(images,[("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])
    def test_extract_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        links = extract_markdown_links(text)
        self.assertEqual(links,[("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")])
class TestConversion(unittest.TestCase):
    def test_tn_to_hn(self):
        node = TextNode("A picture of a penguin",TextType.image,"https://upload.wikimedia.org/wikipedia/commons/a/a3/Aptenodytes_forsteri_-Snow_Hill_Island%2C_Antarctica_-adults_and_juvenile-8.jpg")
        node2 = LeafNode("img","",{"src":"https://upload.wikimedia.org/wikipedia/commons/a/a3/Aptenodytes_forsteri_-Snow_Hill_Island%2C_Antarctica_-adults_and_juvenile-8.jpg","alt":"A picture of a penguin"})
        self.assertEqual(text_node_to_html_node(node).to_html(),node2.to_html())
class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.text)
        new_nodes = split_nodes_delimiter([node], "**", TextType.bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.text),
                TextNode("bolded", TextType.bold),
                TextNode(" word", TextType.text),
            ],
            new_nodes,
        )

    def test_split(self):
        node = TextNode("This is text with a `code block` word", TextType.text)
        new_nodes = split_nodes_delimiter([node], "`", TextType.code)
        expected_nodes = [TextNode("This is text with a ", TextType.text),TextNode("code block", TextType.code),TextNode(" word", TextType.text)]
        self.assertEqual(new_nodes,expected_nodes)
   
    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.text
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.text),
                TextNode("bolded", TextType.bold),
                TextNode(" word and ", TextType.text),
                TextNode("another", TextType.bold),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.text
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.text),
                TextNode("bolded word", TextType.bold),
                TextNode(" and ", TextType.text),
                TextNode("another", TextType.bold),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", TextType.text)
        new_nodes = split_nodes_delimiter([node], "*", TextType.italic)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.text),
                TextNode("italic", TextType.italic),
                TextNode(" word", TextType.text),
            ],
            new_nodes,
        )
    def test_and_italic(self):
        new_nodes = [TextNode("bold",TextType.bold),TextNode(" and *italic*",TextType.text)]
        new_nodes2 = split_nodes_delimiter(new_nodes, "*", TextType.italic)
        self.assertListEqual(
            [
                TextNode("bold", TextType.bold),
                TextNode(" and ", TextType.text),
                TextNode("italic", TextType.italic),
            ],
            new_nodes2
        )
    
    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.text)
        new_nodes = split_nodes_delimiter([node], "`", TextType.code)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.text),
                TextNode("code block", TextType.code),
                TextNode(" word", TextType.text),
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()
