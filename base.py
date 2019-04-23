# -*- coding: utf-8 -*-
import requests

def get_page(natas_idx, username, password, url_appending=None, headers=None, cookies=None, byte=False):
    url = f"http://natas{natas_idx}.natas.labs.overthewire.org/"
    if url_appending:
        url += url_appending
    response = requests.get(url, auth=(username, password), headers=headers, cookies=cookies)
    if not byte:
        content = response.content.decode("utf-8")
    else:
        content = response.content
    return content

def post_page(natas_idx, username, password, data=None, url_appending=None, headers=None, cookies=None, files=None, response_time=False):
    url = f"http://natas{natas_idx}.natas.labs.overthewire.org/"
    if url_appending:
        url += url_appending
    response = requests.post(url, auth=(username, password), data=data, headers=headers, cookies=cookies, files=files)
    content = response.content.decode("utf-8")

    if response_time:
        return response.elapsed.total_seconds(), content

    return content

