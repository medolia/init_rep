# 已无效
import requests
import re
import json


def open_url(keyword, page=1):
    # &s=0 表示从第1个商品开始显示，由于1页是44个商品，所以 &s=44 表示第二页
    # &sort=sale-desc 表示按销量排序
    # param 变量会自动提取字典内的键与值并填入 url 中
    payload = {'q': keyword, 's': str((page - 1) * 44), "sort": "sale-desc"}
    url = "https://s.taobao.com/search"
    headers = {
        'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'
    }

    res = requests.get(url, params=payload, headers=headers)

    return res


# 获取列表页的所有商品
def get_items(res):
    g_page_config = re.search(r'g_page_config = (.*?);\n', res.text)
    page_config_json = json.loads(g_page_config.group(1))
    page_items = page_config_json['mods']['itemlist']['data']['auctions']

    results = []  # 整理出我们关注的信息（ID、标题、链接、售价、销量和商家）
    for each_item in page_items:
        dict1 = dict.fromkeys(
            ('nid', 'title', 'detail_url', 'view_price', 'view_sales', 'nick'))
        dict1['nid'] = each_item['nid']
        dict1['title'] = each_item['title']
        dict1['detail_url'] = each_item['detail_url']
        dict1['view_price'] = each_item['view_price']
        dict1['view_sales'] = each_item['view_sales']
        dict1['nick'] = each_item['nick']
        results.append(dict1)

    return results


# 统计该页面所有商品的销量
def count_sales(items):
    count = 0
    for each in items:
        if '小甲鱼' in each['title']:
            count += int(re.search(r'\d+', each['view_sales']).group())

    return count


def main():
    keyword = input("请输入搜索关键词：")

    length = 3
    total = 0

    for each in range(length):
        res = open_url(keyword, each + 1)
        items = get_items(res)
        total += count_sales(items)

    print("总销量是：", total)


if __name__ == "__main__":
    main()
