from textnode import TextNode, TextType

def main():
    new_obj = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(new_obj)

if __name__ == "__main__":
    main()