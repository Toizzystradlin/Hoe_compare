# в проге Xenu получаешь огромный список всех ссылок на сайте. Сохраняешь в текстовый формат (там с TAB чето)
# открываешь в екселе через данные-получение внешних данных-из текста
# ну и сохраняешь в папку с этой прогой


import requests
from bs4 import BeautifulSoup
import xlrd

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 YaBrowser/19.10.2.195 Yowser/2.5 Safari/537.36'}
#link = 'https://telly-pitera.com/anket/pics/1171/1.jpg'
#открываем файл
rb = xlrd.open_workbook('TelkiPitera.xlsx')
#rb = xlrd.open_workbook('TelkiPitera.xlsx',formatting_info=True)
#выбираем активный лист
sheet = rb.sheet_by_index(0)

name = 1
for row in range(sheet.nrows):   #число строк 
    if sheet.cell_value(row, 3) == 'image/jpeg':
        try:
            link = sheet.cell_value(row, 0)
            photo = requests.get(link, headers=headers).content
            with open('samples/' + str(name) + link[-4:], 'wb') as f:    #link[-4:] это '.jpg'    записывает в папку samples, хз создаст ли она автоматом ее
                f.write(photo)
            print('фотка: ' + str(row) + link + ' скачалась' + ' имя ' + str(name) + link[-4:])
        except: print('фотка: ' + str(row) + link + ' ОШИБКА!!!')
        name = name + 1
print(sheet.nrows)
