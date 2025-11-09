import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("<p>", "This is an HTML Node", [1, 2, 3], {})
        node2 = HTMLNode("<p>", "This is an HTML Node", [1, 2, 3], {})
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = HTMLNode(None, "Something")
        node2 = HTMLNode(None, "Something else")
        self.assertNotEqual(node, node2)

    def test_props(self):
        props = {}
        props["href"] = "https://www.google.com"
        props["target"] = "_blank"
        props_string = ""
        for key in props:
            props_string += f' {key}={props[key]}'
        node = HTMLNode("<p>", "This is a test node", [], props)
        self.assertEqual(node.props_to_html(), props_string)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_with_props(self):
        node = LeafNode("p", "Hey, guys", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<p href="https://www.google.com">Hey, guys</p>')


if __name__ == "__main__":
    unittest.main()
