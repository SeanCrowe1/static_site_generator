import os
import shutil

from copystatic import copy_files_recursive
from gencontent import generate_page

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    for current_dir, subdirs, files in os.walk(dir_path_content):
        for file in files:
            if file.endswith(".md"):
                from_path = os.path.join(current_dir, file)
                inter_path = from_path.replace("./content", "./public")
                root, ext = os.path.splitext(inter_path)
                dest_path = root + ".html"
                generate_page(
                    from_path,
                    template_path,
                    dest_path
                )

    print("Generating pages...")
    generate_page(
        os.path.join(dir_path_content, "index.md"),
        template_path,
        os.path.join(dir_path_public, "index.html"),
    )


main()
