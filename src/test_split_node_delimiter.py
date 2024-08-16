import unittest

from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode

class TestTextNodeToHTMLNode(unittest.TestCase):
	def test_code(self):
		node = TextNode("This is text with a `code block` word", "code")
		html_node = split_nodes_delimiter([node], "`", "code")
		expected_results = [
    		TextNode("This is text with a ", "text", None),
    		TextNode("code block", "code", None),
    		TextNode(" word", "text", None),
		]
		self.assertEqual(new_nodes, expected_results)

	def test_bold(self):
		node = TextNode("This is text with a **bolded** word", "bold")
		html_node = split_nodes_delimiter([node], "**", "bold")
		expected_results = [
    		TextNode("This is text with a ", "text", None),
    		TextNode("bolded", "bold", None),
    		TextNode(" word", "text", None),
		]
		self.assertEqual(new_nodes, expected_results)

	def test_text(self):
		node = TextNode("This is text", "text")
		html_node = split_nodes_delimiter([node], "", "text")
		expected_results = [
    		TextNode("This is text", "text", None)
		]
		self.assertEqual(new_nodes, expected_results)

	def test_text(self):
		node = TextNode("This is text", "link")
		html_node = split_nodes_delimiter([node], "", "text")
		expected_results = [
    		TextNode("This is text", "text", None)
		]
		self.assertEqual(new_nodes, expected_results)

	def test_image(self):
		node = TextNode("This is an image", "image", "https://www.boot.dev")
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, "img")
		self.assertEqual(html_node.value, "")
		self.assertEqual(
			html_node.props,
			{"src": "https://www.boot.dev", "alt": "This is an image"},
		)

if __name__ == "__main__":
	unittest.main()
