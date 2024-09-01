import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):

	def test_extract_title(self):
		md = """
# Tolkien Fan Club

**I like Tolkien**. Read my [first post here](/majesty) (sorry the link doesn't work yet)

> All that is gold does not glitter

## Reasons I like Tolkien
"""
		result = extract_title(md)
		expected_result = "Tolkien Fan Club"
		self.assertEqual(
			result, 
			expected_result
		)