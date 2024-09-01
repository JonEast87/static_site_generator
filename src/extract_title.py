def extract_title(markdown):
	lines = markdown.split("\n")
	for line in lines:
		if line.startswith("# "):
			return line.lstrip("#").strip()
	raise ValueError("Every markdown needs a header tag.")