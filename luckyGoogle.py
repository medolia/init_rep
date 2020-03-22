#! python3
# luckyGoogle.py - Open top5 Google search results for the keyword in clipboard

import webbrowser
import pyperclip
import requests
import bs4


def open_url():
    print('百度一下, 你就知道!')
    headers = {
        'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
    }
    if not pyperclip.paste():
        print("Pyperclip is empty!")
    else:
        url = 'https://www.baidu.com/s?wd=' + pyperclip.paste()
    res = requests.get(url, headers=headers)

    return res


def show_result(res):
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    tgt = soup.find_all(class_="t")
    linkNum = min(5, len(tgt))
    for i in range(linkNum):
        webbrowser.open(tgt[i].find("a")["href"])


def main():
    res = open_url()
    show_result(res)


if __name__ == "__main__":
    main()
