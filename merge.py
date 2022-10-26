# -*- coding: utf-8 -*-
# @Time    : 2022/10/26 12:36
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

url_animeTrackerList = 'https://raw.githubusercontent.com/DeSireFire/animeTrackerList/master/AT_all.txt'

f2 = []

wget.download(url_XIU2)
wget.download(url_animeTrackerList)

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
f1 = open('./tracker.txt','r',encoding='utf-8').readlines()
f3 = open('./sukebei.txt','r',encoding='utf-8').readlines()
f4 = open('./AT_all.txt','r',encoding='utf-8').readlines()

def del_newline(file_lines):
    data_lines = []
    for f in file_lines:
        line_str = f.strip()
        data_lines.append(line_str)
    return data_lines

f1_data = del_newline(f1)
f3_data = del_newline(f3)
f4_data = del_newline(f4)

all = list(set(f1_data+f2+f3_data+f4_data))

with open('./SpaceLine_All.txt','w',encoding='utf-8') as fall:
    data_str = ""
    for a in range(0,len(all)):
        if a == len(all)-1:
            data_str = data_str + all[a]
        else:
            data_str = data_str + all[a] + '\n'+ '\n'
    fall.write(data_str)
    fall.close()

with open('./aria2_all.txt','w',encoding='utf-8') as fall:
    data_str = ""
    for a in range(0,len(all)):
        if a == len(all)-1:
            data_str = data_str + all[a]
        else:
            data_str = data_str + all[a] + ','
    fall.write(data_str)
    fall.close()

with open('./default_all.txt','w',encoding='utf-8') as fall:
    data_str = ""
    for a in range(0,len(all)):
        if a == len(all)-1:
            data_str = data_str + all[a]
        else:
            data_str = data_str + all[a] + '\n'
    fall.write(data_str)
    fall.close()


os.remove('./tracker.txt')
os.remove('./all.txt')
os.remove('./AT_all.txt')
