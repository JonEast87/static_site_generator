class TextNode:
	def __init__(self, text, text_type, url):
		self.text = text
		self.text_type = text_type
		self.url = url

	def __eg__(self, textNode):
		return (
			self.text == textNode.text,
			self.text_type == textNode.text_type,
			self.url == textNode.url
		)

	def __repr__(self):
		return f'TextNode("{self.text}, {self.text_type}, {self.url}")'