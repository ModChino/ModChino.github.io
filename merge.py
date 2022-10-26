# -*- coding: utf-8 -*-
# @Time    : 2022/10/26 12:10
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

f2 = []

wget.download(url_XIU2)

itmxz_data = requests.get(url_itmxz,headers).text

with open('./tracker.txt','w',encoding='utf-8') as fp:
    fp.write(itmxz_data)
    fp.close()

with open('./all.txt', 'r', encoding='utf-8') as fp:
    fp_list = list(set(fp.readlines()))
    for line in fp_list:
        line = line.split('\n')[0]
        if len(line) != 0:
            f2.append(line)
    fp.close()

#去重

f1_data = []
f3_data = []

f1 = open('./tracker.txt','r',encoding='utf-8').readlines()
f3 = open('./sukebei.txt','r',encoding='utf-8').readlines()

for one in f1:
    o = one.strip()
    f1_data.append(o)

for thr in f3:
    t = thr.strip()
    f3_data.append(t)


all = list(set(f1_data+f2+f3_data))

with open('./all-of-all.txt','w',encoding='utf-8') as fall:
    data_str = ""
    for a in range(0,len(all)):
        if a == len(all)-1:
            data_str = data_str + all[a]
        else:
            data_str = data_str + all[a] + '\n'+ '\n'
    fall.write(data_str)
    fall.close()

os.remove('./tracker.txt')
os.remove('./all.txt')
