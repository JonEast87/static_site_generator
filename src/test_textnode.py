import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
	def test_eq(self):
		node1 = TextNode("This is a text node", "bold", "http://boot.dev")
		node2 = TextNode("This is a text node", "bold", "http://boot.dev")
		self.assertEqual(node1, node2)

	def test_eq_text(self):
		node1 = TextNode("This is a text node", "bold", "http://boot.dev")
		node2 = TextNode("This is a different text node", "bold", "http://boot.dev")
		self.assertEqual(node1, node2)


if __name__ == "__main__":
	unittest.main()