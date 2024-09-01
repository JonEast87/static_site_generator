import os, shutil
from markdown_blocks import markdown_to_html_node

def generate_page(from_path, template_path, dest_path):
	print(f"Generating page from {from_path} to {dest_path} using {template_path}")
	open_markdown = open(from_path, "r")
	read_markdown = open_markdown.read()

	open_template = open(template_path, "r")
	read_template = open_template.read()

	title = extract_title(read_markdown)
	md_html_node = markdown_to_html_node(read_markdown).to_html()
	
	read_template = read_template.replace("{{ Title }}", title)
	read_template = read_template.replace("{{ Content }}", md_html_node)

	dir_path = os.path.dirname(dest_path)

	if not os.path.isdir(dir_path):
		os.makedir(dir_path)

	write_html = open(dest_path, "w")
	wrote_html = write_html.write(read_template)


def extract_title(markdown):
	lines = markdown.split("\n")
	for line in lines:
		if line.startswith("# "):
			return line.lstrip("#").strip()
	raise ValueError("Every markdown needs a header tag.")