# coding=utf-8
'''
@File    :   update_host_for_normalGit_linux.py
@Time    :   2024/07/29
@Author  :   xlwang 
'''

'''
# https://raw.hellogithub.com/hosts
# /etc/hosts
'''
import requests
import os
import chardet
import sys

def check_charset(file_path):
    with open(file_path, 'rb') as f:
        data = f.read(4)
        charset = chardet.detect(data)['encoding']
    return charset

def update_host_for_normalGit():
    # update host
    _path = '/etc/hosts'
    with open(_path, encoding=check_charset(_path)) as f:
        old_cont = [s.strip() for s in f.readlines()]
    mark_start = '# >>>github dns start'
    mark_end = '# >>>github dns end'
    if mark_start not in old_cont:
        old_cont.append(mark_start)
        old_cont.append(mark_end)
    update_ind1 = old_cont.index(mark_start)
    update_ind2 = old_cont.index(mark_end)
    # download latest dns maps
    _url = 'https://raw.hellogithub.com/hosts'
    _file = requests.get(_url)
    gitdns_maps = str(_file.content, encoding='utf-8')
    gitdns_maps = [s+'\n' for s in gitdns_maps.split('\n')]
    new_cont = [s+'\n' for s in old_cont[:update_ind1+1]] + gitdns_maps + \
            [s+'\n' for s in old_cont[update_ind2:]]
    with open(_path, 'w') as f:
        f.writelines(new_cont)

update_host_for_normalGit()