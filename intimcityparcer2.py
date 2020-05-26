# -*- coding: utf-8 -*-
"""
Created on Tue May 26 10:48:45 2020

@author: Yuron
"""

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time
import random


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 YaBrowser/19.10.2.195 Yowser/2.5 Safari/537.36'}
t = [i for i in range(350700,350800)] #Диапазон анкет, это почти всегда шестизначное число
random.shuffle(t)
c = 1
a = 1
i = 0
file_name = '1'
while (c <= 100):
    try:
        html = requests.get('https://www.intimcity.nl/persons.php?id=' + str(t[i]), headers=headers).text
        soup = BeautifulSoup(html, 'lxml')
        for link in soup.find_all('img', {'class': 'rnd5'}):
        # print(link.get('src'))
            photo = requests.get(link.get('src'), headers=headers).content
            with open(file_name + '.png', 'wb') as f:
                f.write(photo)
                a = a+1
                file_name = str(a) 
                time.sleep(random.uniform(3, 5))
    except:
        continue
            
    c+=1
    a+=100
    i+=1
    file_name = str(a)
    time.sleep(random.uniform(4, 6))
    