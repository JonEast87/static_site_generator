from textnode import TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
	new_nodes_list = list()
	for old_node in old_nodes:
		if old_node.text_type == "text":
			new_nodes_list.append(old_node)
			return new_nodes_list
		else:
			old_nodes_split = old_node.text.split(f"{delimiter}")
			return_node = iterate_nodes(old_nodes_split, text_type)
			new_nodes_list.extend(return_node)
			return new_nodes_list

		raise Exception("Unsupported text_type!")

# Helper function to check for text types versus styled types
def iterate_nodes(old_nodes_split, text_type):
	text_list = list()
	for node in old_nodes_split:
		if node.endswith(" "):
			text_list.append(TextNode(node, "text"))
		elif node.startswith(" "):
			text_list.append(TextNode(node, "text"))
		else:
			text_list.append(TextNode(node, text_type))
	return text_list
