# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import time
import random
import csv


def get_page(url_one):
    cookies = {
        'Hm_lvt_0e023fed85d2150e7d419b5b1f2e7c0f': '1701649687',
        'Hm_lvt_91cf34f62b9bedb16460ca36cf192f4c': '1701649687',
        'Hm_lvt_a6458082fb548e5ca7ff77d177d2d88d': '1701649705',
        'deviceId': 'ffe3ad3-c3ce-43bf-a588-21bd50d59',
        'sessionId': 'S_0LPQBOYL40EFHQKF',
        'hnUserTicket': 'a6f3b61b-ac0a-45e8-833a-041ba407c80a',
        'hnUserId': '940575415',
        'Hm_lvt_b99541cbfb0edd202bb49abf3a0bef84': '1701664875',
        'Hm_lpvt_b99541cbfb0edd202bb49abf3a0bef84': '1701664875',
        'Hm_lvt_81fc10bb72f85b5a9ff93042925f6543': '1701672935',
        'Hm_lpvt_81fc10bb72f85b5a9ff93042925f6543': '1701674308',
        'Hm_lpvt_0e023fed85d2150e7d419b5b1f2e7c0f': '1701674453',
        'Hm_lpvt_91cf34f62b9bedb16460ca36cf192f4c': '1701674453',
        'Hm_lpvt_a6458082fb548e5ca7ff77d177d2d88d': '1701674453',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # 'Cookie': 'Hm_lvt_0e023fed85d2150e7d419b5b1f2e7c0f=1701649687; Hm_lvt_91cf34f62b9bedb16460ca36cf192f4c=1701649687; Hm_lvt_a6458082fb548e5ca7ff77d177d2d88d=1701649705; deviceId=ffe3ad3-c3ce-43bf-a588-21bd50d59; sessionId=S_0LPQBOYL40EFHQKF; hnUserTicket=a6f3b61b-ac0a-45e8-833a-041ba407c80a; hnUserId=940575415; Hm_lvt_b99541cbfb0edd202bb49abf3a0bef84=1701664875; Hm_lpvt_b99541cbfb0edd202bb49abf3a0bef84=1701664875; Hm_lvt_81fc10bb72f85b5a9ff93042925f6543=1701672935; Hm_lpvt_81fc10bb72f85b5a9ff93042925f6543=1701674308; Hm_lpvt_0e023fed85d2150e7d419b5b1f2e7c0f=1701674453; Hm_lpvt_91cf34f62b9bedb16460ca36cf192f4c=1701674453; Hm_lpvt_a6458082fb548e5ca7ff77d177d2d88d=1701674453',
        'Referer': 'https://www.cnhnb.com/p/hng/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    response = requests.get(url_one, cookies=cookies, headers=headers)
    html_code = response.text
    # print(html_code)
    soup = BeautifulSoup(html_code, 'html.parser')
    total = soup.find('span', class_='eye-pagination__total')
    total_count = int(total.text.replace("共 ", "").replace(" 条", ""))
    page = total_count // 20 + 1
    return page


def html_text(url):
    cookies = {
        'Hm_lvt_0e023fed85d2150e7d419b5b1f2e7c0f': '1701649687',
        'Hm_lvt_91cf34f62b9bedb16460ca36cf192f4c': '1701649687',
        'Hm_lvt_a6458082fb548e5ca7ff77d177d2d88d': '1701649705',
        'deviceId': 'ffe3ad3-c3ce-43bf-a588-21bd50d59',
        'sessionId': 'S_0LPQBOYL40EFHQKF',
        'hnUserTicket': 'a6f3b61b-ac0a-45e8-833a-041ba407c80a',
        'hnUserId': '940575415',
        'Hm_lpvt_a6458082fb548e5ca7ff77d177d2d88d': '1701664848',
        'Hm_lpvt_0e023fed85d2150e7d419b5b1f2e7c0f': '1701664868',
        'Hm_lvt_b99541cbfb0edd202bb49abf3a0bef84': '1701664875',
        'Hm_lpvt_b99541cbfb0edd202bb49abf3a0bef84': '1701664875',
        'Hm_lpvt_91cf34f62b9bedb16460ca36cf192f4c': '1701664892',
    }
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        # 'Cookie': 'Hm_lvt_0e023fed85d2150e7d419b5b1f2e7c0f=1701649687; Hm_lvt_91cf34f62b9bedb16460ca36cf192f4c=1701649687; Hm_lvt_a6458082fb548e5ca7ff77d177d2d88d=1701649705; deviceId=ffe3ad3-c3ce-43bf-a588-21bd50d59; sessionId=S_0LPQBOYL40EFHQKF; hnUserTicket=a6f3b61b-ac0a-45e8-833a-041ba407c80a; hnUserId=940575415; Hm_lpvt_a6458082fb548e5ca7ff77d177d2d88d=1701664848; Hm_lpvt_0e023fed85d2150e7d419b5b1f2e7c0f=1701664868; Hm_lvt_b99541cbfb0edd202bb49abf3a0bef84=1701664875; Hm_lpvt_b99541cbfb0edd202bb49abf3a0bef84=1701664875; Hm_lpvt_91cf34f62b9bedb16460ca36cf192f4c=1701664892',
        'Referer': 'https://www.cnhnb.com/p/jiuhuang-0-0-0-0-1/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    response = requests.get(url, cookies=cookies, headers=headers)
    # print(response.text)
    html_code = response.text
    soup = BeautifulSoup(html_code, 'html.parser')
    # 找到包含信息的元素
    active_cols = soup.find_all('div', class_='active-col')
    # 提取文本内容
    categories = [col.find('a').text.strip() for col in active_cols]
    items = soup.find_all('div', class_='supply-item')
    time.sleep(random.uniform(0.5, 1.4))
    return categories, items


# 打印结果

def get_commodity(categories, items, count_list):
    for item in items:
        title_h2 = item.find('h2')
        shop_price_div = item.find('div', class_='shops-price')
        price_span = shop_price_div.find('span')
        # 提取价格和单位
        price = price_span.text.strip()
        unit = shop_price_div.contents[-1].strip()  # 获取最后一个子元素的文本内容
        shop_name_a = item.find('a', class_='l-shop-btm')
        shop_address_div = item.find('div', class_='r-shop-btm')
        # 提取店名和地址
        shop_name = shop_name_a.text.strip() if shop_name_a else "N/A"
        shop_address = shop_address_div.text.strip() if shop_address_div else "N/A"

        shop_url_a = item.find('a', class_='com-bg')
        # 提取URL
        shop_url = shop_url_a['href'] if shop_url_a else "N/A"
        shop_url = "https://www.cnhnb.com" + shop_url
        # province = get_province(shop_address)
        # 打印URL
        data = {
            "大类别": categories[0],
            "小类别": categories[1],
            "名称": categories[2],
            "标题": title_h2.text.strip(),
            "价格": price,
            "单位": unit,
            "店名": shop_name,
            "地址": shop_address,
            # "省份": province,
            "url": shop_url
        }
        count_list.append(data)
        write_to_csv(data, filename="农产品数据.csv")
        print(f">>>获取第{len(count_list)}条数据{data}")


def get_province(shop_address):
    cookies = {
        'c_y_g_j': '218',
        'Hm_lvt_bd706f26d2267b54fd3543ceaea48e96': '1701668386',
        '__gads': 'ID=93651c1cf5120fa6:T=1701668389:RT=1701668389:S=ALNI_Maf8HQzBaGa_IPrNY0y3EF3_bkZyA',
        '__gpi': 'UID=00000ca483aba574:T=1701668389:RT=1701668389:S=ALNI_MZf5Z09PE2ya4bk4NMVL74epmO_eA',
        'Hm_lpvt_bd706f26d2267b54fd3543ceaea48e96': '1701668391',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # 'Cookie': 'c_y_g_j=218; Hm_lvt_bd706f26d2267b54fd3543ceaea48e96=1701668386; __gads=ID=93651c1cf5120fa6:T=1701668389:RT=1701668389:S=ALNI_Maf8HQzBaGa_IPrNY0y3EF3_bkZyA; __gpi=UID=00000ca483aba574:T=1701668389:RT=1701668389:S=ALNI_MZf5Z09PE2ya4bk4NMVL74epmO_eA; Hm_lpvt_bd706f26d2267b54fd3543ceaea48e96=1701668391',
        'Referer': 'https://xingzhengquhua.bmcx.com/%E7%95%8C%E7%89%8C%E6%9D%91__xingzhengquhua/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    response = requests.get(f'https://xingzhengquhua.bmcx.com/{shop_address}__xingzhengquhua/', cookies=cookies,
                            headers=headers)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    address = soup.find('ul', class_='list')
    province = address.find('li')
    # 提取地址文本
    province = province.text.strip().replace(f"{shop_address}", "")
    # print(province)
    return province


def write_to_csv(data, filename):
    """
    import csv
    参数:
    - data: 要写入的数据，以字典形式表示
    - filename: 要写入的CSV文件名
    - 可套入循环追加填写，不会被顶替
    """
    with open(filename, 'a', newline='', encoding='utf_8_sig') as csvfile:
        fieldnames = data.keys()  # 获取字典的键作为CSV文件的列名
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # 检查文件是否已存在，如果不存在，则写入标题行
        if csvfile.tell() == 0:
            writer.writeheader()  # 写入CSV文件的标题行
        # 写入数据
        writer.writerow(data)


if __name__ == '__main__':
    agricultural_products = [
        # "xiaomai",
        # "hng"
        # "dous",
        # "mianhua",
        # "chaye",
        # "chengzi",
        # "huasheng",
        # "lizi",
        # "jinju",
        # "chengzi",
        # "qiezi",
        # "huanggua"
        # "hlb"
        "xigua",
        "suantai",
        "tudou",
        "bc",
        "xhs"
    ]
    for name in agricultural_products:
        # name
        # name = "dami"
        url_one = f"https://www.cnhnb.com/p/{name}-0-0-0-0-1/"
        page = get_page(url_one)
        if page > 100:
           page = random.randint(30,100)
        count_list = []
        for i in range(1, page + 1):
            url = f"https://www.cnhnb.com/p/{name}-0-0-0-0-{i}/"
            print(f">>>正在获取{name}第{i}页数据，共{page}页")
            categories, items = html_text(url)
            get_commodity(categories, items, count_list)
            if i % 10 == 0:
                time.sleep(random.randint(5, 10))
