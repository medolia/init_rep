import requests
import bs4
import os

os.makedirs('230', exist_ok=True)
headers = {
    'user-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
}
url = 'https://taotuhome.com/16013.html'
res = requests.get(url, headers=headers)
soup = bs4.BeautifulSoup(res.text, "html.parser")

tgts = soup.find_all("img")
imgNum = 0
for i in tgts:
    if i["src"].startswith("https") and i["src"].endswith("jpg"):
        print("Downloading img, url: %s" % (i["src"]))
        imgs = requests.get(i["src"], headers=headers, timeout=3).content
        # 为保存 Unicode 编码，使用二进制写入文件。
        imgName = str(imgNum) + '.jpg'
        with open(os.path.join('230', imgName), 'wb') as f:
            f.write(imgs)
        f.close()
        imgNum += 1
    else:
        pass
