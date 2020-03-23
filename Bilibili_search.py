import requests
import bs4
import time


# 打开网页
def open_url(filter_):
    url = "https://search.bilibili.com/all"
    headers = {
        'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'
    }
    res = requests.get(url, params=filter_, headers=headers)
    soup = bs4.BeautifulSoup(res.text, "html.parser")

    return soup


# 收集信息
def get_info(each):
    data = {
        "title": each.a["title"],
        "链接": each.a["href"],
        "播放量": each.find(title="观看").text.strip(),
        "上传时间": each.find(title="上传时间").text.strip()
    }

    return data


def save_info(soup):
    tgts = soup.find_all("li", class_="video-item matrix")
    # 需要指定编码格式，否则默认使用 gbk 编码会出错。
    # 使用附加模式打开 "a"
    file_list = ["综合排序.txt", "最多点击.txt", "最新发布.txt", "最多弹幕.txt", "最多收藏.txt"]
    with open(file_list[order_num], "a", encoding="utf-8") as f:
        for each in tgts:
            data = get_info(each)
            f.write("%s | 播放量:%s | https:%s | %s \n\n" %
                    (data["title"], data["播放量"], data["链接"], data["上传时间"]))
    f.close()


def run(keyword):
    order_list = ["totalrank", "click", "pubdate", "dm", "stow"]
    filter_ = {
        'keyword': keyword,
        'order': order_list[order_num],
        # 0 - 4 : all < 10, 30, 60 >
        "duration": "0",
        "tids_1": "0",
        "page": "1"
    }
    while int(filter_["page"]) <= 10:
        soup = open_url(filter_)
        # 控制访问频率，避免被屏蔽。
        time.sleep(1)
        save_info(soup)
        filter_["page"] = str(int(filter_["page"]) + 1)


def main():
    keyword = str(input("请输入检索关键词: "))
    global order_num
    for order_num in range(5):
        run(keyword)


if __name__ == "__main__":
    main()
