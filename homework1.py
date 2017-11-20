# -*- coding: utf-8 -*-
from __future__ import division  #精确出除法，保留小数位
import re
import numpy as np
from collections import Counter

pr = []
a = []
c = []
proteins = {}

f = open('seq.fa.txt','r')        #打开文件seq.fa，以只读的方式
lines = f.readlines()
for line in lines:
    line = line.strip('\n')       #去掉换行符
    #line = line.replace('\n','') #去掉换行符
    if re.match('[A-Z]',line):    #匹配字母
        pr_tmp = list(line)       #生成列表
        pr.append(pr_tmp)         #生成二维列表
f.close()

f2 = open("frq.txt","w")          #打开文件frq.txt，以写入的方式         
for i in range(0,len(pr)):        #遍历二维数组
    proteins = Counter(pr[i])     #生成字典proteins
    a = proteins.keys()           #获得字典的key
    b = '\t'.join(proteins)       #以tab键连接字典的key
    c = proteins.values()         #获得字典的值
    d = np.sum(c)                 #统计一列值的总和
    f2.write(b)                   #将b通过write函数写入frq.txt文件中
    f2.write("\n")
    for j in c:
        f2.write(str(round((j/d),2)))  #round(x,2)保留2位小数，str(m)变成str
        f2.write("\t")
    f2.write("\n")
f2.close()   