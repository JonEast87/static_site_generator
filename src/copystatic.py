import os, shutil

def copystatic(src, dst):
	copy_files = os.listdir(src)
	if not os.path.exists(dst):
		os.mkdir(dst)

	for copy_file in copy_files:
		from_path = os.path.join(src, copy_file)
		dest_path = os.path.join(dst, copy_file)
		if os.path.isfile(from_path):
			shutil.copy(from_path, dest_path)
		else:
			# Recursive call using loop scoped paths incase a dir needs to be created
			copystatic(from_path, dest_path)