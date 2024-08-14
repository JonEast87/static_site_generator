class HTMLNode:
	def __init__(self, tag=None, value=None, children=None, props=None):
		self.tag = tag if tag is not None else None
		self.value = value if value is not None else None
		self.children = children if children is not None else None
		self.props = props if props is not None else None

	def to_html(self):
		raise NotImplementedError("")

	def props_to_html(self):
		html_attributes = list()
		# Replaced old method to better handle variety of sizes
		for key, value in self.props.items():
			html_attributes.append(f'{key}="{value}"')
		
		return " ".join(html_attributes)

	def __eq__(self, other):
		if isinstance(other, HTMLNode):
			return (
				self.props == other.props
			)
		return False

	def __repr__(self):
		return f'HTMLNode("{self.tag}, {self.value}, {self.children}, {self.props}")'

class LeafNode(HTMLNode):
	def __init__(self, tag, value, props=None):
		super().__init__(tag, value, None, props)
		self.tag = tag
		self.value = value
		self.props = props if props is not None else None

	def to_html(self):
		if self.value == None:
			raise ValueError("All leaf nodes must have a value")

		if self.tag == None:
			return self.value

		html = f"<{self.tag}"

		if self.props:
			props = self.props_to_html()
			html += f" {props}"

		html += f">{self.value}</{self.tag}>"

		return html
