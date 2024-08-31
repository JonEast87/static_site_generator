import os, shutil
from copystatic import copystatic

def main():
	source = "./static"
	destination = "./public"
	print("Deleting public directory...")
	# Replaced the function call since it can be done much easier with a single line of code, oof
	if os.path.exists(destination):
		shutil.rmtree(destination)

	print("Copying static files to public directory...")
	copystatic(source, destination)

main()