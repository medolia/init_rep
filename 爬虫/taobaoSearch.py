import re
import requests
import openpyxl


def getHtml(url):
    headers = {
        'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36',
        'cookie':
        'cna=DqG+FkAemiUCASewKKSFMT7/; thw=cn; lgc=%5Cu6DFC%5Cu97F3%5Cu5E8F%5Cu66F2%5Cu4E4B%5Cu9B44; tracknick=%5Cu6DFC%5Cu97F3%5Cu5E8F%5Cu66F2%5Cu4E4B%5Cu9B44; tg=0; enc=scvPg4IvLZPMyd%2F5i%2FxGa5X8LmZPOadXGr%2FIr0Twqt9gbCVHuYSpbZOd46BXqz0BEDZV7umIa4onvxjS7yN2zw%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; t=28f1797e6458fc3c12f67a479390d85e; mt=ci=-1_1; sgcookie=EnBsYU3X2%2FkQnjRhVELlj; uc3=vt3=F8dBxd9ve%2Fmo4r5XjmY%3D&lg2=URm48syIIVrSKA%3D%3D&id2=UUpmmWufD%2FC%2BYA%3D%3D&nk2=ji2iUjhfbx6x8VyB; uc4=nk4=0%40jIaCgCvnI39KzTjyunHkdqpv07kCpM4%3D&id4=0%40U2gsFU7gwEwHsMj%2FxMhjwnHxSBit; _cc_=W5iHLLyFfA%3D%3D; _m_h5_tk=8e0108f1081c5b3d1ed7825e16b44a3b_1585323914182; _m_h5_tk_enc=f9974d90862251c5d6c3d7a8c7fefe14; tfstk=c9MdBejqUFY3U8s50nAgFHqQ5n8cZyL85Male3G8EoBcCrXRiyDmHYVkOu_LBhC..; v=0; cookie2=506b0ebeee6368192e16fb1436707404; _tb_token_=5ede6e31ea0ee; uc1=cookie14=UoTUP2b8ugP1SA%3D%3D; _samesite_flag_=true; isg=BExMG_CQfh_IEWoXWglfGlUCHap-hfAvpKsKw6YNWPeaMew7zpXAv0KD0TkJYiiH; l=dBxY2vcrQ1EJHK6QBOCanurza77OSIRYYuPzaNbMi_5gK6T1u6QOosKNNF96VjWftxLB4cjscSv9-etkZQDmndK-g3fPaxDc'
    }
    res = requests.get(url, headers=headers)
    res.raise_for_status()

    return res.text


def getInfo(html):
    item_title = re.findall(r'\"raw_title\"\:\".*?\"', html)
    item_price = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
    item_sales = re.findall(r'\"view_sales\"\:\".*?\"', html)
    data = []
    for i in range(len(item_title)):
        data.append([
            item_title[i].split(':')[1], item_price[i].split(':')[1],
            item_sales[i].split(':')[1]
        ])

    return data


def toExcel(data):
    wb = openpyxl.Workbook()
    wb.guess_types = True
    ws = wb.active
    ws.append(['title', 'price', 'sales'])
    for each in data:
        ws.append(each)

    wb.save('sum.xlsx')


def main():
    keyword = str(input("Offer a keyword: "))
    url = 'https://s.taobao.com/search?q=' + keyword
    html = getHtml(url)
    data = getInfo(html)
    toExcel(data)


if __name__ == "__main__":
    main()
