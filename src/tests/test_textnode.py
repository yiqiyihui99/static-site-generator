import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        
        # Test different texttype properties
        node3 = TextNode("This is a different text node type", TextType.ITALIC)
        node4 = TextNode("This is a different text node text", TextType.BOLD)
        self.assertNotEqual(node, node3)
        self.assertNotEqual(node, node4)
        
        # Test different url properties
        node5 = TextNode("This is a text node", TextType.BOLD, "https://www.google.com")
        node6 = TextNode("This is a text node", TextType.BOLD, "https://www.facebook.com")
        self.assertNotEqual(node, node5)
        self.assertNotEqual(node, node6)
        self.assertNotEqual(node5, node6)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_link(self):
        node = TextNode("This is a link", TextType.LINK, "https://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link")
        self.assertEqual(html_node.props["href"], "https://www.google.com")
    
    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "This is an image")
        self.assertEqual(html_node.props["src"], "https://www.google.com")
        self.assertEqual(html_node.props["alt"], "This is an image")
    
    def test_code(self):
        node = TextNode("This is a code", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code")
    
    def test_italic(self):
        node = TextNode("This is an italic", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic")
    
    def test_bold(self):
        node = TextNode("This is a bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold")
        
        
if __name__ == "__main__":
    unittest.main()