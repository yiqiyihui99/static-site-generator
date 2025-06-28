import unittest
from markdown_to_blocks import markdown_to_blocks, block_to_block_type, BlockType

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = "## Hello\n\nThis is a test"
        expected = [
            "## Hello",
            "This is a test",
        ]
        print(markdown_to_blocks(markdown), expected)
    
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    
    def test_block_to_block_type(self):
        self.assertEqual(block_to_block_type("## Hello"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("This is a paragraph"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(">This is a quote/n>With two lines"), BlockType.QUOTE)
        self.assertEqual(block_to_block_type("- This is a list\n- With two items"), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type("1. This is an ordered list\n2. With two items"), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type("```This is a code block```"), BlockType.CODE)