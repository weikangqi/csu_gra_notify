from lxml import etree
import requests
url = "https://gra.csu.edu.cn/yjsytz.htm"

def get_html(url):
    title = 'https://gra.csu.edu.cn/'
    req = requests.get(url)
    req.encoding = 'utf-8'
    tree = etree.HTML(req.text) 
    return tree.xpath('/html/body/section/div[2]/ul/li[1]/div/a')[0].text , title + tree.xpath('/html/body/section/div[2]/ul/li[1]/div/a')[0].attrib['href']

if __name__ == '__main__':
    print(get_html(url))