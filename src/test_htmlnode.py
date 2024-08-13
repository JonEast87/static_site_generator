import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
	def test_props(self):
		node1 = HTMLNode("<a>", "click here", "", {"href": "https://www.google.com", "target": "_blank", })
		self.assertEqual(node1.props_to_html(), "href='https://www.google.com' target='_blank'")

if __name__ == "__main__":
	unittest.main()
