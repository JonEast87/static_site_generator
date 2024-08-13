class HTMLNode:
	def __init__(self, tag=None, value=None, children=None, props=None):
		self.tag = tag if tag is not None else None
		self.value = value if value is not None else None
		self.children = children if children is not None else None
		self.props = props if props is not None else None

	def to_html(self):
		raise NotImplementedError("")

	def props_to_html(self):
		access_keys = self.props.keys()
		access_keys_list = list(access_keys)
		return f"{access_keys_list[0]}='{self.props['href']}' {access_keys_list[1]}='{self.props['target']}'"

	def __eq__(self, other):
		if isinstance(other, HTMLNode):
			return (
				self.props == other.props
			)
		return False

	def __repr__(self):
		return f'HTMLNode("{self.tag}, {self.value}, {self.children}, {self.props}")'
