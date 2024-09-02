import os, shutil
from pathlib import Path
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

	dest_dir_path = os.path.dirname(dest_path)
	if dest_dir_path != "":
		os.makedirs(dest_dir_path, exist_ok=True)
	write_html = open(dest_path, "w")
	write_html.write(read_template)


def extract_title(markdown):
	lines = markdown.split("\n")
	for line in lines:
		if line.startswith("# "):
			return line.lstrip("#").strip()
	raise ValueError("Every markdown needs a header tag.")

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
	for filename in os.listdir(dir_path_content):
		from_path = os.path.join(dir_path_content, filename)
		dest_path = os.path.join(dest_dir_path, filename)

		if os.path.isfile(from_path):
			dest_path = Path(dest_path).with_suffix(".html")
			generate_page(from_path, template_path, dest_path)
		# if os.path.isdir(f):
		# 	if not os.path.exists(os.path.join(dest_dir_path, filename)):
		else:
			# os.mkdir(os.path.join(dest_dir_path, filename))
			# Recursive call, passing `f` as the dir_path instead similar to copystatic
			generate_pages_recursive(from_path, template_path, dest_path)