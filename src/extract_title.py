
def extract_title(markdown: str):
    for line in markdown.split("\n"):
        if line.startswith("# "):
            return line.lstrip("#").strip()
    
    raise Exception("No title found")
