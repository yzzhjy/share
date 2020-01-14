# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 16:58:58 2020

@author: yzzhj
"""

from random import choice
if __name__ == '__main__':
    total = 100000
    k = []
    time = 0
for j in range(total):
    choose = choice([1,2,3])          
    if choose == 1:
        time+=4
    elif choose==2:
        time+=6
    else:
        time+=2
        k.append(time)
        time = 0            
s = 0
for i in k:
    s+= i
print(s/len(k))