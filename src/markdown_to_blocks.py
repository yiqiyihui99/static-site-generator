from enum import Enum
import re

def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = markdown.split("\n\n")
    out_blocks = []
    for block in blocks:
        block = block.strip()
        if block == "":
            continue
        out_blocks.append(block)
    return out_blocks

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block: str) -> BlockType:
    if re.match(r"^#{1,6}\s", block):
        return BlockType.HEADING
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    split_block = block.split("\n")
    is_quote = True
    is_unordered_list = True
    is_ordered_list = True
    count = 1
    for line in split_block:
        if not line.startswith(">"):
            is_quote = False
        if not line.startswith("- "):
            is_unordered_list = False
        if not line.startswith(f"{count}. "):
            is_ordered_list = False
        else:
            count += 1
    if is_quote:
        return BlockType.QUOTE
    if is_unordered_list:
        return BlockType.UNORDERED_LIST
    if is_ordered_list:
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH