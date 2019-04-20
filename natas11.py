# -*- coding: utf-8 -*-
from base import get_page, post_page
import re
from subprocess import Popen, PIPE

def natas11():
    username = "natas11"
    password = "U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK"
    stdout, stderr = Popen("php natas11.php", shell=True, stdout=PIPE, stderr=PIPE).communicate()
    if stderr:
        print("Fail to find password")
        return
    data = stdout.decode("utf-8")
    cookies = {"data":data}
    content = get_page(11, username, password, cookies=cookies)
    password = re.search(r"(?<=The password for natas12 is )\w{32}", content)
    if password is None:
        print("Fail to find password")
        return
    print(password.group(0))


if __name__ == "__main__":
    natas11()

