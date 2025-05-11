import unittest

from htmlnode import HTMLNODE, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        # Test blank initialization + instantiation
        blank_htmlnode = HTMLNODE()
        self.assertEqual(blank_htmlnode.tag, None)
        self.assertEqual(blank_htmlnode.value, None)
        self.assertEqual(blank_htmlnode.children, None)
        self.assertEqual(blank_htmlnode.props, None)    
        
        # Test props_to_html
        htmlnode1 = HTMLNODE(props={"href": "https://www.google.com", "target": "_blank"})
        htmlnode2 = HTMLNODE(props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(htmlnode1.props_to_html(), htmlnode2.props_to_html())
        
        htmlnode3 = HTMLNODE(props={"href": "https://www.youtube.com", "target": "_blank"})
        self.assertNotEqual(htmlnode1.props_to_html(), htmlnode3.props_to_html())
        
        # Test to_html
        with self.assertRaises(NotImplementedError):
            htmlnode1.to_html()
            
    def test_leaf_node(self):
        # Test blank initialization + instantiation
        with self.assertRaises(TypeError):
            blank_leaf_node = LeafNode()
        
        # Test to_html
        node = LeafNode(tag="p", value="Hello, p-tag!")
        self.assertEqual(node.to_html(), "<p>Hello, p-tag!</p>")
        
        node1 = LeafNode(tag="a", value="Hello, a-tag!")
        self.assertEqual(node1.to_html(), "<a>Hello, a-tag!</a>")
        # # Test props_to_html (inherited from HTMLNODE)
        # node2 = LeafNode(tag="p", value="Hello, world!", props={"href": "https://www.google.com", "target": "_blank"})
        # self.assertEqual(node2.props_to_html(), "href=https://www.google.com target=_blank")
        
    def test_parent_node(self):
        # Test blank initialization + instantiation
        with self.assertRaises(TypeError):
            blank_parent_node = ParentNode()
        
        # Test to_html
        node = ParentNode(tag="p", children=[LeafNode(tag="b", value="Bold text"), LeafNode(tag="i", value="Italic text")])
        self.assertEqual(node.to_html(), "<p><b>Bold text</b><i>Italic text</i></p>")
        
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_with_multiple_children(self):
        child_node1 = LeafNode("span", "child1")
        child_node2 = LeafNode("span", "child2")
        parent_node = ParentNode("div", [child_node1, child_node2])
        self.assertEqual(parent_node.to_html(), "<div><span>child1</span><span>child2</span></div>")
    
        
