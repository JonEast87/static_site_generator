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

def split_nodes_image(old_nodes):
	new_nodes_list = list()
	for old_node in old_nodes:
		image_extraction = extract_markdown_images(old_node.text)
		if len(image_extraction) == 0:
			new_nodes_list.append(old_node)

		else:
			text_list = list()
			new_node_text = old_node.text
			for alt_text, image_link in image_extraction:
				sections = new_node_text.split(f"![{alt_text}]({image_link})", 1)
				text_list.append(sections[0])
				# Assigning next sections index to be split on the next outer loop passover
				new_node_text = sections[1]
			for l, image_tup in enumerate(image_extraction):
				if text_list[l].strip(): # Avoid empty content
					new_nodes_list.append(TextNode(text_list[l], text_type_text))
				new_nodes_list.append(TextNode(image_tup[0], text_type_image, image_tup[1]))
			if new_node_text.strip(): # Ensures empty content is not appended
				new_nodes_list.append(TextNode(new_node_text, text_type_text))
			return new_nodes_list

def split_nodes_link(old_nodes):
	new_nodes_list = list()
	for old_node in old_nodes:
		link_extraction = extract_markdown_links(old_node.text)
		if len(link_extraction) == 0:
			new_nodes_list.append(old_node)

		else:
			text_list = list()
			new_node_text = old_node.text
			for link_text, link_link in link_extraction:
				sections = new_node_text.split(f"[{link_text}]({link_link})", 1)
				text_list.append(sections[0])
				# Assigning next sections index to be split on the next outer loop passover
				new_node_text = sections[1]
			for l, link_tup in enumerate(link_extraction):
				if text_list[l].strip(): # Avoid empty content
					new_nodes_list.append(TextNode(text_list[l], text_type_text))
				new_nodes_list.append(TextNode(link_tup[0], text_type_link, link_tup[1]))
			if new_node_text.strip(): # Ensures empty content is not appended
				new_nodes_list.append(TextNode(new_node_text, text_type_text))
			return new_nodes_list

def text_to_textnodes(text):
	base_text_node = [TextNode(text, "text")]
	text_node_list = split_nodes_delimiter(base_text_node, "**", "bold")
	text_node_list = split_nodes_delimiter(text_node_list, "*", "italic")
	text_node_list = split_nodes_delimiter(text_node_list, "`", "code")
	text_node_list = split_nodes_image(text_node_list)
	text_node_list = split_nodes_link(text_node_list)
	return text_node_list