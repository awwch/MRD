# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 12:13:56 2016

@author: Ania
"""
import re
import csv

def open_dict(path):
    f = open(path,'r',encoding = 'utf-8')
    _dict = f.read().split('<div class="superEntry">')
    f.close()
    return _dict
_dict = open_dict('gs_html.txt')
    
table = csv.reader(open('abbs.csv'), delimiter=';', quotechar='"')
abbs = []
for row in table:
    abbs.append(row)

for art in _dict:
    if art == '':
        _dict.remove(art)
    else:
        