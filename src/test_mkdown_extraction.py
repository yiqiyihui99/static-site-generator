import unittest

from mkdown_extraction import extract_markdown_links, extract_markdown_images


class TestMkdownExtraction(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = "This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) \
            and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected = [("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_markdown_links(self):
        text = "This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) \
            and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif")]
        self.assertEqual(extract_markdown_links(text), expected)

if __name__ == "__main__":
    unittest.main()
