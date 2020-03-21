import requests
import bs4

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
res = requests.get('https://www.google.com/maps/', headers=headers)

# 检查是否成功下载网页
try:
    res.raise_for_status()
except Exception as exc:
    print('There is a problem: %s' % (exc))


soup = bs4.BeautifulSoup(res.text, 'html.parser')

# with open('temp_html.txt', 'w', encoding='utf-8') as f:
#     for chunk in res:
#         f.write(chunk)

# f.close()
