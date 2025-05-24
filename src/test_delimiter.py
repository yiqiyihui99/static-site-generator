import unittest

from delimiter import split_nodes_delimiter
from textnode import TextNode, TextType

class TestDelimiter(unittest.TestCase):
    def test_split_nodes_delimiter_missing_closing(self):
        nodes = [TextNode("This is a **bold text node", TextType.TEXT)]
        delimiter = "**"
        text_type = TextType.BOLD
        
        # Should raise a ValueError because there's no closing delimiter
        with self.assertRaises(ValueError):
            split_nodes_delimiter(nodes, delimiter, text_type)
    
    def test_split_nodes_delimiter_text(self):
        nodes = [TextNode("This is a text node", TextType.TEXT)]
        delimiter = "**"
        text_type = TextType.BOLD
        split_nodes = split_nodes_delimiter(nodes, delimiter, text_type)
        
        expected = [TextNode("This is a text node", TextType.TEXT)]
        self.assertEqual(split_nodes, expected)
    
    def test_split_nodes_delimiter_bold(self):
        nodes = [TextNode("This is a **bold** text node", TextType.TEXT)]
        delimiter = "**"
        text_type = TextType.BOLD
        split_nodes = split_nodes_delimiter(nodes, delimiter, text_type)
        
        expected = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text node", TextType.TEXT)
        ]
        self.assertEqual(split_nodes, expected)
    
    def test_split_nodes_delimiter_italic(self):
        nodes = [TextNode("This is an *italic* text node", TextType.TEXT)]
        delimiter = "*"
        text_type = TextType.ITALIC
        split_nodes = split_nodes_delimiter(nodes, delimiter, text_type)
        
        expected = [
            TextNode("This is an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text node", TextType.TEXT)
        ]
        self.assertEqual(split_nodes, expected)
    
    def test_split_nodes_delimiter_code(self):
        nodes = [TextNode("This is a `code` text node", TextType.TEXT)]
        delimiter = "`"
        text_type = TextType.CODE
        split_nodes = split_nodes_delimiter(nodes, delimiter, text_type)
        
        expected = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" text node", TextType.TEXT)
        ]
        self.assertEqual(split_nodes, expected)
    
    def test_multiple_delimiters(self):
        nodes = [TextNode("This has **two** **bold** sections", TextType.TEXT)]
        delimiter = "**"
        text_type = TextType.BOLD
        split_nodes = split_nodes_delimiter(nodes, delimiter, text_type)
        
        expected = [TextNode("This has ", TextType.TEXT), 
                    TextNode("two", TextType.BOLD),
                    TextNode(" ", TextType.TEXT),
                    TextNode("bold", TextType.BOLD),
                    TextNode(" sections", TextType.TEXT)
                    ]

        self.assertEqual(split_nodes, expected)
    