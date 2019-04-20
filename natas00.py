# -*- coding: utf-8 -*-
from base import get_page 
import re


username = "natas0"
password = "natas0"
content = get_page(0, username, password)
password = re.search(r"(?<=The password for natas1 is )\w+", content)
if password is not None:
    print(password.group(0))
else:
    print("Fail to find password")