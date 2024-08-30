import os, shutil

def main():
	destination = "./public/"
	source = "./static/"

	delete_files = os.listdir(destination)
	copy_files = os.listdir(source)

	for file in delete_files:
		if os.path.exists(destination + file):
			if os.path.isfile(destination + file):
				os.remove(destination + file)
			if os.path.isdir(destination + file):
				shutil.rmtree(destination + file)

	for copy_file in copy_files:
		if os.path.exists(source + copy_file):
			if os.path.isfile(source + copy_file):
				shutil.copy(source + copy_file, destination)
			if os.path.isdir(source + copy_file):
				# Will replace this to do it recursively, since that is what the assignment calls for
				shutil.copytree(source + copy_file, destination + copy_file)

main()