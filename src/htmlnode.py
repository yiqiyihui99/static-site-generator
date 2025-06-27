class HTMLNODE:
    def __init__(self, tag: str = None, value: str = None, children: list = None, props: dict = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self):
        raise NotImplementedError("HTMLNODE doesn't implement to_html()")

    def props_to_html(self):
        if self.props is None:
            return ""
        props_str = ""
        for key, value in self.props.items():
            props_str += f' {key}="{value}"'
        return props_str
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
    
class LeafNode(HTMLNODE):
    def __init__(self, tag: str, value: str, props: dict = None):
        super().__init__(tag=tag, value=value, props=props, children=None)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("Leaf node has no value")
        elif self.tag is None:
            return self.value
        else:
            props_html = self.props_to_html()
            # Special handling for self-closing tags
            if self.tag == "img":
                return f"<{self.tag}{props_html}>"
            return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"

class ParentNode(HTMLNODE):
    def __init__(self, tag: str, children: list, props: dict = None):
        super().__init__(tag=tag, value=None, props=props, children=children)
        
    def to_html(self):
        if self.tag is None:
            raise ValueError("Parent node has no tag")
        elif self.children is None:
            raise ValueError("Parent node has no children")
        else:
            children_html = ""
            for child in self.children:
                children_html += child.to_html()
            props_html = self.props_to_html()
            return f"<{self.tag}{props_html}>{children_html}</{self.tag}>"
    