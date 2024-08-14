import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
	def test_props(self):
		node1 = HTMLNode("<a>", "click here", "", {"href": "https://www.google.com", "target": "_blank", })
		self.assertEqual(node1.props_to_html(), 'href="https://www.google.com" target="_blank"')

	def test_to_html(self):
		leaf1 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
		self.assertEqual(leaf1.to_html(), '<a href="https://www.google.com">Click me!</a>')

	def test_parent_to_html(self):
		parent1 = ParentNode(
    		"p",
		    [
		        LeafNode("b", "Bold text"),
		        LeafNode(None, "Normal text"),
		        LeafNode("i", "italic text"),
		        LeafNode(None, "Normal text"),
		    ],
		)
		self.assertEqual(parent1.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

if __name__ == "__main__":
	unittest.main()
