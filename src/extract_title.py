def extract_title(markdown):
	lines = markdown.split("\n")
	for line in lines:
		split_line = line.split(" ")
		if split_line[0] == "#":
			removed_tag = line.strip("#")
			removed_whitespace = removed_tag.strip()
			return removed_whitespace

	raise Exception("Every markdown needs a header tag.")
