'''
    需求：获取网址 http://www.mzitu.com/all/  下最新月份的的所有妹子图片，并分文件夹放入 meizitu 文件夹中
    最终目录结构如: meizitu/18岁MM久久Aimee：可以甜美也可以狂野的御姐养成记/29c01.jpg
'''
import os
import logging

import re
import requests
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO)


def store_girl_img(girl_url, store_girl_dir):
    # 把girl_url的单个小姐姐放入store_girl_dir文件夹
    girl_text = requests.get(girl_url).text
    print(girl_text)
    girl_src = BeautifulSoup(girl_text, 'lxml').find("div",class_='content-pic').find("a")
    print(girl_src)
    # 此处加headers是为防反爬虫，如果不加会响应403，没有权限
    headers = {
        'Referer': girl_url,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    file_name = girl_src.split('/')[-1]
    file_name = os.path.join(store_girl_dir, file_name)
    with open(file_name, 'wb') as f:
        girl_content = requests.get(girl_src, headers=headers).content
        f.write(girl_content)


def store_page_grils(href, store_girl_dir):
    # 把href这个链接下的小姐姐们（多个）放入文件夹store_girl_dir
    girl_text = requests.get(href).text
    soup = BeautifulSoup(girl_text, 'lxml')
    # 得到小姐姐的数量
    max_page_num = soup.find('div', class_='content-page').find_all('a')[-2].get_text()
    max_page_num = int(max_page_num)
    # print(max_page_num)

    for page_num in range(1, max_page_num + 1):
        girl_url = f'{href}/{str(page_num)}'
        print(girl_url,"----------------------------")      #http://www.mm131.com/mingxing/2016_3.html
        store_girl_img(girl_url, store_girl_dir)


def main():
    url = 'http://www.mm131.com/mingxing'
    store_dir = 'meizitu'
    os.makedirs(store_dir, exist_ok=True)
    home_html = requests.get(url)
    home_html.encoding = "gbk"
    home_text = home_html.text
    #print(home_text)
    # 得到小姐姐们的链接标签
    ahref_list = BeautifulSoup(home_text, 'lxml').find("div",class_="main").find('dd').find_all("a")
    print(ahref_list)
    for ahref in ahref_list:
        # ahref 是bs4.element.Tag实例
        girlname = ahref.get_text()  # 获取a标签的文本内容
        print(girlname)
        #print(type(ahref))
        href = ahref.attrs["href"]
        print(href)
  # 取出a标签的href属性
        # print(href)
        store_girl_dir = os.path.join(store_dir, girlname)  # 拼接得到放该小姐的房间号，即存放美女的文件夹
        os.makedirs(store_girl_dir, exist_ok=True)
        logging.info(f'开始下载{girlname}的图片')
        store_page_grils(href, store_girl_dir)


if __name__ == '__main__':
    main()
