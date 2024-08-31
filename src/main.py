import os, shutil

def delete(dst):
	delete_files = os.listdir(dst)
	for file in delete_files:
		if os.path.exists(dst + file):
			if os.path.isfile(dst + file):
				os.remove(dst + file)
			if os.path.isdir(dst + file):
				shutil.rmtree(dst + file)

def copy(src, dst):
	copy_files = os.listdir(src)
	for copy_file in copy_files:
		if os.path.exists(src + copy_file):
			if os.path.isfile(src + copy_file):
				shutil.copy(src + copy_file, dst)
			if os.path.isdir(src + copy_file):
				# Will replace this to do it recursively, since that is what the assignment calls for
				shutil.copytree(src + copy_file, dst + copy_file)

def main():
	source = "./static/"
	destination = "./public/"
	delete(destination)
	copy(source, destination)

main()