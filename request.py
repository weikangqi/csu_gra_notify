from lxml import etree
import requests
import sqlite3
url = "https://gra.csu.edu.cn/yjsytz.htm"

def get_html(url):
    title = 'https://gra.csu.edu.cn/'
    req = requests.get(url)
    req.encoding = 'utf-8'
    tree = etree.HTML(req.text) 
    news = tree.xpath('/html/body/section/div[2]/ul/li') #一页中所有的新闻
    new_of_one_Web = len(news)
    total = [] #所有新闻的标题,和url
    for i in range(new_of_one_Web):
        total.append((tree.xpath(f'/html/body/section/div[2]/ul/li[{i+1}]/div/a')[0].text,title + tree.xpath(f'/html/body/section/div[2]/ul/li[{i+1}]/div/a')[0].attrib['href']))
    return total

if __name__ == '__main__':
    print(get_html(url))