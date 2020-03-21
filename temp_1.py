import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    target = 'https://www.17k.com/chapter/88532/2754092.html'
    req = requests.get(url=target)
    html = req.text
    bf = BeautifulSoup(html)
    texts = bf.find_all('div', class_='readAreaBox content')
    print(req.text)
