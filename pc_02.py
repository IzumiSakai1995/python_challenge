# -*- coding: utf-8 -*-
# @Time    : 2018/07/12 18:33:47
# @Author  : Izumi Sakai
# @File    : pc_02.py
# @Software: PyCharm
import requests
import re
url = 'http://www.pythonchallenge.com/pc/def/ocr.html'
response = requests.get(url)
mess_str = ''.join(re.findall('<!--(.*)-->',response.text,re.S))
print(''.join(re.findall('[a-z]',mess_str)))
