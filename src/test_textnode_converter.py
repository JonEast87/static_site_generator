import unittest

from textnode_converter import text_node_to_html_node
from htmlnode import HTMLNode, LeafNode
from textnode import TextNode

class TestTextConveter(unittest.TestCase):
	def test_font_decorator(self):
		setup_node = TextNode("This is a test", "italic")
		test_func = text_node_to_html_node(setup_node)
		self.assertEqual(test_func, HTMLNode("i", "This is a test", None, None))

	def test_image(self):
		setup_node = TextNode("", "image", "https://www.thislink.com")
		print(setup_node.text_type)
		test_func = text_node_to_html_node(setup_node)
		self.assertEqual(test_func, HTMLNode("img", "", None, { "src": "https://www.thislink.com", "alt": "" }))

if __name__ == "__main__":
	unittest.main()