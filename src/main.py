from textnode import TextNode, TextType

def main():
    dummynode = TextNode("This is an anchor test", TextType.LINK, "https://www.boot.dev")
    print(repr(dummynode))
    
if __name__ == "__main__":
    main()