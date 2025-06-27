from markdown_to_blocks import markdown_to_blocks, block_to_block_type, BlockType
from htmlnode import HTMLNODE, LeafNode, ParentNode
from text_to_textnodes import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType

def markdown_to_html_node(markdown_text: str) -> HTMLNODE:
    blocks = markdown_to_blocks(markdown_text)
    html_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        html_nodes.append(block_type_to_html_node(block_type, block))
    return ParentNode("div", html_nodes)

def block_type_to_html_node(block_type: BlockType, block: str) -> HTMLNODE:
    match block_type:
        case BlockType.PARAGRAPH:
            block = " ".join(block.split())
            return ParentNode("p", text_to_children(block))
        case BlockType.HEADING:
            level = len(block.split()[0])  # Count # symbols
            return ParentNode(f"h{level}", text_to_children(block.lstrip("# ")))
        case BlockType.CODE:
            # Remove the ``` markers and preserve the exact content between them
            # Split into lines and remove first and last line (the ``` markers)
            lines = block.split("\n")
            if len(lines) >= 2:
                # Remove first line (opening ```) and last line (closing ```)
                code_lines = lines[1:-1]
                
                # Find the minimum indentation (ignoring empty lines)
                min_indent = float('inf')
                for line in code_lines:
                    if line.strip():  # Only consider non-empty lines
                        indent_len = len(line) - len(line.lstrip())
                        min_indent = min(min_indent, indent_len)
                
                # If all lines were empty, set min_indent to 0
                if min_indent == float('inf'):
                    min_indent = 0
                
                # Remove the common indentation from all lines
                dedented_lines = []
                for line in code_lines:
                    if len(line) >= min_indent:
                        dedented_lines.append(line[min_indent:])
                    else:
                        dedented_lines.append(line)
                
                # Join the content lines
                code_content = "\n".join(dedented_lines)
                # Add a trailing newline if there's content
                if code_content:
                    code_content += "\n"
            else:
                code_content = ""
            # Create a TextNode with TEXT type (not CODE) to avoid inline parsing
            # Then convert it to HTMLNode and wrap in code tag
            text_node = TextNode(code_content, TextType.TEXT)
            code_node = text_node_to_html_node(text_node)
            return ParentNode("pre", [ParentNode("code", [code_node])])
        case BlockType.QUOTE:
            # Strip "> " from the beginning of each line
            lines = block.split("\n")
            cleaned_lines = [line.lstrip("> ") for line in lines]
            # Join the lines with spaces
            quote_text = " ".join(cleaned_lines)
            # Collapse multiple spaces into single spaces
            quote_text = " ".join(quote_text.split())
            return ParentNode("blockquote", text_to_children(quote_text))
        case BlockType.UNORDERED_LIST:
            items = [item.lstrip("- ") for item in block.split("\n")]
            return ParentNode("ul", [ParentNode("li", text_to_children(item)) for item in items])
        case BlockType.ORDERED_LIST:
            items = [item.split(". ", 1)[1] for item in block.split("\n")]
            return ParentNode("ol", [ParentNode("li", text_to_children(item)) for item in items])

def text_to_children(text: str) -> list[HTMLNODE]:
    text_nodes = text_to_textnodes(text)
    return [text_node_to_html_node(node) for node in text_nodes]