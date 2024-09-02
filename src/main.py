import os, shutil
from copystatic import copystatic
from gencontent import generate_pages_recursive

def main():
	source = "./static"
	destination = "./public"
	content = "./content"
	template = "./template.html"
	print("Deleting public directory...")
	if os.path.exists(destination):
		shutil.rmtree(destination)

	print("Copying static files to public directory...")
	copystatic(source, destination)

	print("Generating page...")
	generate_pages_recursive(content, template, destination)

main()