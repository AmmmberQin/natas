# -*- coding: utf-8 -*-
from base import get_page
import re

username = "natas1"
password = "gtVrDuiDfck831PqWsLEZy5gyDz1clto"
content = get_page(1, username, password)
password = re.search(r"(?<=The password for natas2 is )\w+", content)
if password is not None:
    print(password.group(0))
else:
    print("Fail to find password")