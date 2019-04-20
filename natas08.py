# -*- coding: utf-8 -*-
from base import get_page, post_page
import re
import base64
from subprocess import Popen, PIPE

def natas8():
    username = "natas8"
    password = "DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe"
    stdout, stderr = Popen("php natas08.php", shell=True, stdout=PIPE, stderr=PIPE).communicate()
    if stderr:
        print("Fail to find password")
        return
    secret = stdout.decode("utf-8")
    data={"secret": secret,"submit": "Submit"}
    content = post_page(8, username, password, data=data)
    password = re.search(r"(?<=natas9 is )\w{32}", content)
    if password is None:
        print("Fail to find password")
        return
    print(password.group(0))


if __name__ == "__main__":
    natas8()