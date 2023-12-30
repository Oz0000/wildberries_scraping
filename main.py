import requests
from bs4 import BeautifulSoup
from time import sleep
from fake_useragent import UserAgent as ua
import json


headers = {
    'Accept': '*/*',
    'Connection': 'keep-alive',
    'Origin': 'https://www.wildberries.ru',
    'Referer': 'https://www.wildberries.ru/catalog/muzhchinam/odezhda/dzhinsy',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': ua().random,
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'x-requested-with': 'XMLHttpRequest'
}

data = {
   'TestGroup': 'mmr_14',
   'TestID': '388',
   'appType': '1',
   'cat': '8149',
   'curr': 'rub',
   'dest': '-1257786',
   'page': '1',
   'sort': 'popular',
   'spp': '27',
}

response = requests.get('https://catalog.wb.ru/catalog/men_clothes2/catalog', params=data, headers=headers)


result = []
item_info = {}

temp = response.json()
for i in temp['data']['products']:
    item_info['Brand'] = i['brand']
    item_info['Jeans_name'] = i['name']
    item_info['Jeans info'] = [{'colors': [j['name'] for j in i['colors']]}]
    item_info['Brand info'] = [{'grade': i['reviewRating'], 'review count': i['feedbacks'], 'supplier': i['supplier'], 'supplier rating': i['supplierRating']}]
    item_info['Price'] = int(str(i['salePriceU'])[:-2])

    result.append(item_info)
    item_info = {}



with open('mens-jeans-result.json', 'w', encoding='utf-8') as file:
    json.dump(result, file, indent=4, ensure_ascii=False)








