#! python3
# luckyGoogle.py - Open top5 Google search results for the keyword in clipboard

import webbrowser
import pyperclip
import requests
import bs4

# define searching engine
print('百度一下, 你就知道!')
headers = {
    'user-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
}
url = 'https://www.baidu.com/s?wd=' + pyperclip.paste()
res = requests.get(url, headers=headers)

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, "html.parser")

# Open a browser tab for each result.
# 结果数可能小于 5
tgt = soup.find_all(class_="t")
linkNum = min(5, len(tgt))
for i in range(linkNum):
    webbrowser.open(tgt[i].find("a")["href"])
