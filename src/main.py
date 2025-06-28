from textnode import TextNode, TextType
import os
import shutil
from generate_page import generate_page

def main():
    source_to_dest("src/static", "public/")
    generate_page("content/index.md", "template.html", "public/index.html")
    
# This function takes all contents from a source directory into a
# destination directory (public)
def source_to_dest(source_dir, dest_dir):
    if not os.path.exists(source_dir):
        raise FileNotFoundError(f"Source directory {source_dir} does not exist")
    
    os.makedirs(dest_dir, exist_ok=True)
    
    for item in os.listdir(dest_dir):
        item_path = os.path.join(dest_dir, item)
        if os.path.isdir(item_path):
            print(f"Removing directory {item_path}")
            shutil.rmtree(item_path)
        else:
            print(f"Removing file {item_path}")
            os.remove(item_path)
    
    for item in os.listdir(source_dir):
        src_path = os.path.join(source_dir, item)
        dst_path = os.path.join(dest_dir, item)
        if os.path.isdir(src_path):
            print(f"Copying directory {src_path} to {dst_path}")
            source_to_dest(src_path, dst_path)
        else:
            print(f"Copying item {item} from {src_path} to {dst_path}")
            shutil.copy(src_path, dst_path)
            
if __name__ == "__main__":
    main()