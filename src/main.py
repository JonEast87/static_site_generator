import os, shutil

def main():
	destination = "./public/"
	source = "./static/"

	delete_files = os.listdir(destination)
	copy_files = os.listdir(source)
	# for file in delete_files:
	# 	if os.path.exists(destination + file):
	# 		os.remove(destination + file)
	# 	if os.path.isdir(destination + file):
	# 		shutil.rmtree(destination + file)

	for copy_file in copy_files:
		if os.path.exists(source + copy_file) and os.path.isfile(source + copy_file):
			shutil.copy(source + copy_file, destination)
		if os.path.isdir(source + copy_file):
			try:
				shutil.copytree(source + copy_file, destination + copy_file)
			except:
				raise Exception(source + copy_file)
		else:
			# For debugging
			print(destination + copy_file)

main()