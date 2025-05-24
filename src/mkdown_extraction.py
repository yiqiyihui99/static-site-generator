import re

# in: raw markdown text
# out: list of tuples (alt text, image url)
#
def extract_markdown_images(text) -> list[tuple[str, str]]:
    images = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return images

def extract_markdown_links(text) -> list[tuple[str, str]]:
    links = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return links

