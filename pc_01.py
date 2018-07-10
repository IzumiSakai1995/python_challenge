# -*- coding: utf-8 -*-
# @Time    : 2018/07/10 22:54:36
# @Author  : Izumi Sakai
# @File    : pc_01.py
# @Software: PyCharm

import requests
from bs4 import BeautifulSoup
def main():
    url = 'http://www.pythonchallenge.com/pc/def/map.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'lxml')
    print(soup.findAll("br"))



if __name__ == '__main__':
    main()
