# Задание №1
# � Написать программу, которая считывает список из 10 URLадресов и одновременно загружает данные с каждого
# адреса.
# � После загрузки данных нужно записать их в отдельные
# файлы.
# � Используйте потоки.

import os
import requests
import threading
import time

urls = ['https://www.google.ru/',
'https://gb.ru/',
'https://ya.ru/',
'https://www.python.org/',
'https://habr.com/ru/all/',
'https://pegast.ru/',
'https://ozon.ru/',
'https://bgoperator.ru/',
'https://wildberries.ru/',
'https://tourdom.ru/',
]


def download(url):
    response = requests.get(url)
    dir_name = 'thread'
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    filename = dir_name + '/' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
    with open(filename, "w", encoding='utf-8') as f:
        f.write(response.text)
    print(f"Downloaded {url} in {time.time()-start_time:.2f} seconds")


threads = []
start_time = time.time()

for url in urls:
    thread = threading.Thread(target=download, args=[url])
    threads.append(thread)
    thread.start()
    
for thread in threads:
    thread.join()