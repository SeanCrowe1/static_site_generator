class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise(NotImplementedError)
    
    def props_to_html(self):
        if self.props == {} or self.props == None:
            return ""
        
        complete = ""
        for key in self.props:
            complete += f' {key}={self.props[key]}'
        return complete
    
    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return NotImplemented
        return (
            self.tag == other.tag
            and self.value == other.value
            and self.children == other.children
            and self.props == other.props
        )
    
    def __repr__(self):
        return f'HTMLNode( {self.tag} | {self.value} | {self.children} | {self.props} )'
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value == None:
            raise(ValueError)
        if self.tag == None:
            return self.value
        
        attrs = ""
        if self.props:
            attrs = "".join(f' {k}="{v}"' for k, v in self.props.items())
        
        return f'<{self.tag}{attrs}>{self.value}</{self.tag}>'