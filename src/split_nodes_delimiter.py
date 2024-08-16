from textnode import TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
	new_nodes_list = list()
	old_nodes_split = old_nodes[0].text.split(f"{delimiter}")
	if text_type == "link" or text_type == "image":
		new_nodes_list.extend(old_nodes)
	else:
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
