from htmlnode import ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node

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


markdown_text = """
# Tolkien Fan Club

**I like Tolkien**. Read my [first post here](/majesty) (sorry the link doesn't work yet)

> All that is gold does not glitter

## Reasons I like Tolkien

* You can spend years studying the legendarium and still not understand its depths
* It can be enjoyed by children and adults alike
* Disney *didn't ruin it*
* It created an entirely new genre of fantasy

## My favorite characters (in order)

1. Gandalf
2. Bilbo
3. Sam
4. Glorfindel
5. Galadriel
6. Elrond
7. Thorin
8. Sauron
9. Aragorn

Here's what `elflang` looks like (the perfect coding language):

```
func main(){
    fmt.Println("Hello, World!")
}
```
"""

def markdown_to_html(markdown):
	blocks = markdown_to_blocks(markdown)
	htmlnode_list = list()
	for block in blocks:
		html_node = block_to_html_node(block)
		htmlnode_list.append(html_node)
	return ParentNode("div", htmlnode_list, None)

def block_to_html_node(block):
	if tag == "heading":
			header = 0
			for char in block:
				if char == "#":
					header += 1
			new_htmlnode = HTMLNode(f"h{header}", block)
			htmlnode_list.append(new_htmlnode)
	if tag == "unordered_list":
		new_htmlnode = HTMLNode("ul", block)
		htmlnode_list.append(new_htmlnode)
	if tag == "ordered_list":
		new_htmlnode = HTMLNode("ol", block)
		htmlnode_list.append(new_htmlnode)
	if tag == "code":
		new_htmlnode = HTMLNode("code", block)
		htmlnode_list.append(new_htmlnode)
	if tag == "quote":
		new_htmlnode = HTMLNode("blockquote", block)
		htmlnode_list.append(new_htmlnode)
	if tag == "paragraph":
		new_parentnode = HTMLNode("p", block)
		htmlnode_list.append(new_htmlnode)

def text_to_children(text):
	text_nodes = text_to_textnodes(text)
	children = list()
	for text_node in text_nodes:
		html_node = text_node_to_html_node(text_node)
		children.append(html_node)
	return children

def heading_to_html_node(block):
	if tag == "heading":
		header = 0
		for char in block:
			if char == "#":
				header += 1
			else:
				break
		if level + 1 >= len(block):
			raise ValueError(f"Invalid heading level: {level}")
		text = block[level + 1 :]
		children = texst_to_children(text)
		return ParentNode(f"h{level}", children)

def code_to_html_node(block):
	if not block.startswith("```") or not block.endswith("```"):
		raise ValueError("Invalid code block")
	text = block[4:-3]
	children = texst_to_children(text)
	code = ParentNode("code", children)
	return ParentNode("pre", [code])

output = markdown_to_html(markdown_text)
print(output)