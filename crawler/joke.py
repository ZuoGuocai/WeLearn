#!/usr/bin/env python
# author: zuoguocai@126.com

import requests
from bs4 import BeautifulSoup


def joke(page):
    url = "https://www.qiushibaike.com/text/page/" + str(page) + "/"
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
    }
    response = requests.get(url,headers=header)
    html=response.text

    soup = BeautifulSoup(html,'lxml')

    articles = soup.find_all(class_='article')
    
    story_list = []
    for div in articles:
        author = div.h2.get_text().strip()
        content =div.find(class_="content").get_text().strip()
        number=div.find(class_="number").get_text().strip()
        story_list.append([author,content,number])
    
    return(story_list)


if  __name__ == '__main__':
    for page  in range(1,14):
        bypage = joke(page)
        print(bypage)
