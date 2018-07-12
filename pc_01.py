# -*- coding: utf-8 -*-
# @Time    : 2018/07/10 22:54:36
# @Author  : Izumi Sakai
# @File    : pc_01.py
# @Software: PyCharm

from urllib.request import urlopen
from bs4 import BeautifulSoup
def main():
    url = 'http://www.pythonchallenge.com/pc/def/map.html'
    response = urlopen(url)
    soup = BeautifulSoup(response,'lxml')
    result = soup.findAll("br")
    print(result[0].get_text())



if __name__ == '__main__':
    main()
