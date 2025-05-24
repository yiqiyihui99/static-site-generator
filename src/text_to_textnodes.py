from textnode import TextNode, TextType
from delimiter import split_nodes_delimiter
from split_nodes import split_nodes_image, split_nodes_link

def extend_unique(list1, list2):
    for item in list2:
        if item not in list1:
            list1.append(item)
    return list1



def text_to_textnodes(input_text: str) -> list[TextNode]:
    node_representation = TextNode(input_text, TextType.TEXT)
    
    bold_splitted = split_nodes_delimiter([node_representation], "**", TextType.BOLD)
    italic_splitted = split_nodes_delimiter(bold_splitted, "_", TextType.ITALIC)
    code_splitted = split_nodes_delimiter(italic_splitted, "`", TextType.CODE)
    image_splitted = split_nodes_image(code_splitted)
    link_splitted = split_nodes_link(image_splitted)
    final_splitted = link_splitted
            
    return final_splitted


