# 套图之家爬取套图.py

import requests
import bs4
import os
import random


def open_url(url):
    # 基础设置
    global headers
    headers = {
        'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
    }
    res = requests.get(url, headers=headers)
    soup = bs4.BeautifulSoup(res.text, "html.parser")

    return soup


def get_urls(soup):
    # 获取图片的 url
    list_urls = [
        url.get('data-lazy-src')
        for url in soup.select('div.single-content >p >img')
    ]

    return list_urls


def img_info(soup):
    # 获取图片信息(暂仅获取套图名)
    series_name = soup.find("h1", class_="entry-title").text

    return series_name


def save_imgs(list_urls, series_name):
    # 保存图片, timeout 默认为 5, 如经常发生 timeout 错误可适当增加 timeout 值
    os.makedirs(series_name, exist_ok=True)
    imgNum = len(list_urls)
    print("开始下载套图: %s" % (series_name))
    for i in range(imgNum):
        imgs = requests.get(list_urls[i], headers=headers, timeout=5).content
        imgName = str(i) + '.jpg'
        with open(os.path.join(series_name, imgName), 'wb') as f:
            f.write(imgs)
        f.close()
        print("已下载: %s" % (imgName))
    print("下载完成！")


def main():
    # 主程序
    series_Num = str(input("请输入神秘代码(为空则随机获取): "))
    if not series_Num:
        series_Num = random.randint(100, 15000)
    url = 'https://taotuhome.com/' + str(series_Num) + '.html'
    m = open_url(url)
    m_list = get_urls(m)
    series_name = img_info(m)
    save_imgs(m_list, series_name)


if __name__ == "__main__":
    main()
