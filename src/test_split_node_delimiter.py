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
		self.assertEqual(html_node, expected_results)

	def test_bold(self):
		node = TextNode("This is text with a **bolded** word", "bold")
		html_node = split_nodes_delimiter([node], "**", "bold")
		expected_results = [
    		TextNode("This is text with a ", "text", None),
    		TextNode("bolded", "bold", None),
    		TextNode(" word", "text", None),
		]
		self.assertEqual(html_node, expected_results)

	def test_text(self):
		node = TextNode("This is text", "text")
		html_node = split_nodes_delimiter([node], "", "text")
		expected_results = [
    		TextNode("This is text", "text", None)
		]
		self.assertEqual(html_node, expected_results)


if __name__ == "__main__":
	unittest.main()
