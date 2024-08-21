def markdown_to_blocks(markdown):
	split_markdown = markdown.split("\n\n")
	split_block = list()
	for word in split_markdown:
		if word == "":
			continue
		word = word.strip()
		split_block.append(word)
	return split_block