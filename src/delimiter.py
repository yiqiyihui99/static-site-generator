from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    out = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            out.append(node)
            continue

        current_text = node.text
        start_delimiter_index = current_text.find(delimiter)
        if start_delimiter_index == -1:
            out.append(node)
            continue
        
        while start_delimiter_index != -1:
            start_search_position=start_delimiter_index + len(delimiter)
            
            end_delimiter_index = current_text.find(delimiter, start_search_position)
            if end_delimiter_index == -1:
                raise ValueError(f"No closing delimiter '{delimiter}' found")
            
            out.extend([
                TextNode(current_text[:start_delimiter_index], TextType.TEXT),
                TextNode(current_text[start_delimiter_index + len(delimiter):end_delimiter_index], text_type),
                TextNode(current_text[end_delimiter_index + len(delimiter):], TextType.TEXT)
            ])
            break
            
    return out