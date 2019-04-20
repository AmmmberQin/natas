# -*- coding: utf-8 -*-
import requests
from requests_html import HTMLSession

def get_page(natas_idx, username, password, url_appending=None, headers=None, cookies=None):
    url = f"http://natas{natas_idx}.natas.labs.overthewire.org/"
    if url_appending:
        url += url_appending
    response = requests.get(url, auth=(username, password), headers=headers, cookies=cookies)
    content = response.content.decode("utf-8")
    return content

def post_page(natas_idx, username, password, data=None, url_appending=None, headers=None, cookies=None):
    url = f"http://natas{natas_idx}.natas.labs.overthewire.org/"
    if url_appending:
        url += url_appending
    response = requests.post(url, auth=(username, password), data=data, headers=headers, cookies=cookies)
    content = response.content.decode("utf-8")
    return content

def html_get_page(natas_idx, username, password, url_appending=None, headers=None, cookies=None):
    session = HTMLSession()
    url = f"http://natas{natas_idx}.natas.labs.overthewire.org/"
    if url_appending:
        url += url_appending
    response = session.get(url, auth=(username, password), headers=headers, cookies=cookies)
    content = response.html.search('br')
    return content
