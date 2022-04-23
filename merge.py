# -*- coding: utf-8 -*-
# @Time    : 2021/11/15 11:05
# @Author  : Mod
# @Site    : ModChino.github.io
# @File    : merge.py
# @Software: PyCharm
# @Comment :

import requests
import wget
import os

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
}

url_XIU2 = 'https://raw.githubusercontent.com/XIU2/TrackersListCollection/master/all.txt'

url_itmxz = 'http://github.itzmx.com/1265578519/OpenTracker/master/tracker.txt'

wget.download(url_XIU2)

itmxz_data = requests.get(url_itmxz,headers).text

with open('./tracker.txt','w',encoding='utf-8') as fp:
    fp.write(itmxz_data)

with open('./all.txt', 'r', encoding='utf-8') as fp, open('new_all.txt', 'w+', encoding='utf-8') as new_f:
    fp_list = list(set(fp.readlines()))
    for line in fp_list:
        line = line.split('\n')[0]
        if len(line) != 0:
            new_f.writelines(line+"\n")

with open('./new_all.txt','r',encoding='utf-8') as f1,open('./tracker.txt','r',encoding='utf-8') as f2,open('sukebei.txt','r',encoding='utf-8') as f3,open('all-of-all.txt','w+',encoding='utf-8') as f4:
     f4.writelines(f1.readlines())
     f4.writelines(f2.readlines())
     f4.writelines(f3.readlines())
os.remove('./new_all.txt')
os.remove('./tracker.txt')
os.remove('./all.txt')
