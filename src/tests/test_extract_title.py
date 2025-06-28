import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        markdown = "# This is a title"
        title = extract_title(markdown)
        self.assertEqual(title, "This is a title")
        
    def test_extract_title_with_multiple_lines(self):
        markdown = "##This is a title\n\n# This is a subtitle"
        title = extract_title(markdown)
        self.assertEqual(title, "This is a subtitle")
    
    def test_extract_title_with_no_title(self):
        markdown = "This is a subtitle"
        with self.assertRaises(Exception):
            extract_title(markdown)
    
    def test_extract_title_with_multiple_titles(self):
        markdown = "# This is a title\n# This is a subtitle"
        title = extract_title(markdown)
        self.assertEqual(title, "This is a title")     