class HTMLNODE:
    def __init__(self, tag: str = None, value: str = None, children: list = None, props: dict = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self):
        raise NotImplementedError("HTMLNODE doesn't implement to_html()")

    def props_to_html(self):
        return f"href={self.props['href']} targert={self.props['target']}"
    
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
            return f"<{self.tag}>{self.value}</{self.tag}>"

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
            return f"<{self.tag}>{children_html}</{self.tag}>"
    