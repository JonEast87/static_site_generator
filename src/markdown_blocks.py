block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"

def markdown_to_blocks(markdown):
	split_markdown = markdown.split("\n\n")
	split_block = list()
	for word in split_markdown:
		if word == "":
			continue
		word = word.strip()
		split_block.append(word)
	return split_block

def block_to_block_type(block):
	lines = block.split("\n")

	if (
		block.startswith("# ")
		or block.startswith("## ")
		or block.startswith("### ")
		or block.startswith("#### ")
		or block.startswith("##### ")
		or block.startswith("###### ")
	):
		return block_type_heading
	if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
		return block_type_code
	if block.startswith(">"):
		for line in lines:
			if not line.startswith(">"):
				return block_type_paragraph
		return block_type_quote
	if block.startswith("* ") or block.startswith("- "):
		for line in lines:
			if not line.startswith("* ") or line.startswith("- "):
				return block_type_paragraph
		return block_type_ulist
	if block.startswith("1. "):
		i = 1
		for line in lines:
			if not line.startswith(f"{i}. "):
				return block_type_paragraph
			i += 1
		return block_type_olist
	return block_type_paragraph