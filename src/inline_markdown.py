import re

from textnode import (
	TextNode,
	text_type_text,
	text_type_bold,
	text_type_italic,
	text_type_code,
	text_type_link,
	text_type_image,
)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
	new_nodes_list = list()
	for old_node in old_nodes:
		if old_node.text_type != text_type_text:
			new_nodes_list.append(old_node)
			continue

		text_list = list()
		old_nodes_split = old_node.text.split(delimiter)

		if len(old_nodes_split) % 2 == 0:
			raise ValueError("Invalid markdown, format not closed.")
		# Merged the helper here to consolidate
		for node in old_nodes_split:
			if node.endswith(" "):
				text_list.append(TextNode(node, text_type_text))
			elif node.startswith(" "):
				text_list.append(TextNode(node, text_type_text))
			# Added to ensure any styles that end the sentence are not including a blank space
			elif node == "":
				continue
			else:
				text_list.append(TextNode(node, text_type))

		new_nodes_list.extend(text_list)
	return new_nodes_list

def extract_markdown_images(text):
	matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
	return matches

def extract_markdown_links(text):
	matches = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
	return matches