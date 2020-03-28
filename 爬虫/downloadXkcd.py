#! python3
# downloadXkcd.py - Download every single XKCDS comic.

import os
import requests
import bs4

headers = {
    'user-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
}
url = 'https://xkcd.com/'

os.makedirs('xkcd', exist_ok=True)
while not url.endswith('#'):
    print("Downloading page %s..." % url)
    res = requests.get(url, headers=headers)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # select id 属性为 comic 内的 img 元素。
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print("not found!")
    else:
        comicUrl = 'https:' + comicElem[0].get('src')
        print('Downloading image %s' % (comicUrl))
        res = requests.get(comicUrl, headers=headers)
        res.raise_for_status()
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)),
                         'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    preLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com/' + preLink.get('href')

print("Done.")
