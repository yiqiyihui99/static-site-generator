import unittest
from markdown_to_html_node import markdown_to_html_node
from htmlnode import HTMLNODE, LeafNode, ParentNode

class TestMarkdownToHtmlNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
    This is **bolded** paragraph
    text in a p
    tag here

    This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
    ```
    This is text that _should_ remain
    the **same** even with inline stuff
    ```
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_headings(self):
        """Test all heading levels 1-6"""
        md = """# This is an h1

## This is an h2

### This is an h3  

#### This is an h4

##### This is an h5

###### This is an h6"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>This is an h1</h1><h2>This is an h2</h2><h3>This is an h3</h3><h4>This is an h4</h4><h5>This is an h5</h5><h6>This is an h6</h6></div>",
        )

    def test_headings_with_inline_formatting(self):
        """Test headings with inline formatting"""
        md = """# This is a **bold** heading

## This has *italic* and `code` text"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>This is a <b>bold</b> heading</h1><h2>This has <i>italic</i> and <code>code</code> text</h2></div>",
        )

    def test_quote_blocks(self):
        """Test quote blocks"""
        md = """> This is a quote
> with multiple lines
> that should be joined

> This is another quote with **bold** text"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote with multiple lines that should be joined</blockquote><blockquote>This is another quote with <b>bold</b> text</blockquote></div>",
        )

    def test_unordered_lists(self):
        """Test unordered lists"""
        md = """- First item
- Second item
- Third item with **bold**

- Another list
- With two items"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>First item</li><li>Second item</li><li>Third item with <b>bold</b></li></ul><ul><li>Another list</li><li>With two items</li></ul></div>",
        )

    def test_ordered_lists(self):
        """Test ordered lists"""
        md = """1. First item
2. Second item with *italic*
3. Third item

1. New list starts here
2. Second item in new list"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>First item</li><li>Second item with <i>italic</i></li><li>Third item</li></ol><ol><li>New list starts here</li><li>Second item in new list</li></ol></div>",
        )

    def test_multiple_code_blocks(self):
        """Test multiple code blocks with different content"""
        md = """```
def hello():
    print("Hello, World!")
```

Some text between code blocks

```
// JavaScript code
const x = 42;
```"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><pre><code>def hello():\n    print("Hello, World!")\n</code></pre><p>Some text between code blocks</p><pre><code>// JavaScript code\nconst x = 42;\n</code></pre></div>',
        )

    def test_code_block_with_varying_indentation(self):
        """Test code blocks that have different levels of indentation"""
        md = """```
    if (x > 0) {
        console.log("positive");
    } else {
        console.log("non-positive");
    }
```"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><pre><code>if (x > 0) {\n    console.log("positive");\n} else {\n    console.log("non-positive");\n}\n</code></pre></div>',
        )

    def test_empty_code_block(self):
        """Test empty code block"""
        md = """```
```"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code></code></pre></div>",
        )

    def test_mixed_content(self):
        """Test a document with various markdown elements"""
        md = """# My Document

This is a paragraph with **bold** and *italic* text.

## Code Example

Here's some code:

```
print("Hello")
```

## Lists

- Item 1
- Item 2

1. First
2. Second

> A wise quote

The end."""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><h1>My Document</h1><p>This is a paragraph with <b>bold</b> and <i>italic</i> text.</p><h2>Code Example</h2><p>Here\'s some code:</p><pre><code>print("Hello")\n</code></pre><h2>Lists</h2><ul><li>Item 1</li><li>Item 2</li></ul><ol><li>First</li><li>Second</li></ol><blockquote>A wise quote</blockquote><p>The end.</p></div>',
        )

    def test_paragraph_with_links_and_images(self):
        """Test paragraphs with links and images"""
        md = """This is a paragraph with a [link](https://example.com) and an ![image](https://example.com/img.png).

Another paragraph with [another link](https://test.com)."""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><p>This is a paragraph with a <a href="https://example.com">link</a> and an <img src="https://example.com/img.png" alt="image">.</p><p>Another paragraph with <a href="https://test.com">another link</a>.</p></div>',
        )

    def test_whitespace_handling(self):
        """Test proper whitespace handling in different contexts"""
        md = """    This paragraph has leading spaces
    and continues here

```
    This code has spaces
    that should be preserved
```

> Quote with     extra    spaces"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This paragraph has leading spaces and continues here</p><pre><code>This code has spaces\nthat should be preserved\n</code></pre><blockquote>Quote with extra spaces</blockquote></div>",
        )

if __name__ == "__main__":
    unittest.main()