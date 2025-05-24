from textnode import TextNode, TextType

from mkdown_extraction import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes):
    images_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            images_nodes.append(node)
            continue

        images = extract_markdown_images(node.text)

        if not images:
            images_nodes.append(node)
            continue

        remaining_text = node.text

        for image_alt, image_link in images:
            sections = remaining_text.split(f"![{image_alt}]({image_link})", 1)
            remaining_text = sections[1]
            if sections[0]:
                images_nodes.append(TextNode(sections[0], TextType.TEXT))
            images_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
            
            if len(sections) > 1:
                remaining_text = sections[1]
            else:
                remaining_text = ""
        
        if remaining_text:
            images_nodes.append(TextNode(remaining_text, TextType.TEXT))
            
    return images_nodes
    
def split_nodes_link(old_nodes):
    links_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            links_nodes.append(node)
            continue

        links = extract_markdown_links(node.text)

        if not links:
            links_nodes.append(node)
            continue

        remaining_text = node.text

        for link_hypertext, link in links:
            sections = remaining_text.split(f"[{link_hypertext}]({link})", 1)
            if sections[0]:
                links_nodes.append(TextNode(sections[0], TextType.TEXT))
            links_nodes.append(TextNode(link_hypertext, TextType.LINK, link))
            
            if len(sections) > 1:
                remaining_text = sections[1]
            else:
                remaining_text = ""
        
        if remaining_text:
            links_nodes.append(TextNode(remaining_text, TextType.TEXT))
            
    return links_nodes