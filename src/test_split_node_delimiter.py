import unittest

from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode

class TestTextNode(unittest.TestCase):
	def test_eq(self):
		node = TextNode("This is text with a `code block` word", "code")
		new_nodes = split_nodes_delimiter([node], "`", "code")
		expected_results = [
    		TextNode("This is text with a ", "text", None),
    		TextNode("code block", "code", None),
    		TextNode(" word", "text", None),
		]
		self.assertEqual(new_nodes, expected_results)

if __name__ == "__main__":
	unittest.main()
