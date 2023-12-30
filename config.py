# response = requests.get(url=wburl, headers=headers)

## СКАЧИВАНИЕ ГЛАВНОЙ СТРАНИЦЫ WB
# with open('WB Главная.html', 'w', encoding='utf-8') as site:
#     site.write(response.text)

# headers1 = {
#     'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
#     'Referer': 'https://www.wildberries.ru/',
#     'sec-ch-ua-mobile': '?0',
#     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
#     'sec-ch-ua-platform': '"Linux"',
# }
#
# response1 = requests.get('https://static-basket-01.wbbasket.ru/vol0/data/main-menu-ru-ru-v2.json', headers=headers)



# with open('Категории.json', 'w', encoding='utf-8') as file:
#     file.write(response1.text)




# wburl = 'https://www.wildberries.ru'
#
#
# def childs(lst):
#     dct = {}
#     for i in lst:
#         if 'childs' not in i:
#             try:
#                 dct[i['seo']] = i['url']
#             except Exception:
#                 dct[i['name']] = i['url']
#         else:
#             dct.update(childs(i['childs']))
#     return dct
#
#
# # надо переписать под requests
# categories = {}
# upk = {}
# with open('Категории.json', encoding='utf-8') as file:
#     temp = json.loads(file.read())
#     for i in temp:
#         if i['name'] in ['Женщинам', 'Обувь', 'Детям', 'Мужчинам', 'Электроника', 'Зоотовары', 'Спорт']:
#             try:
#                 upk.update(childs(i['childs']))
#             except Exception:
#                 upk[i['name']] = i['url']
#
#             categories[i['name']] = [upk]
#             upk = {}


# input_category = input('Женщинам, Обувь, Детям, Мужчинам, Электроника, Зоотовары, Спорт, What category you want to Scrap').title()

# for item in categories[input_category]:
#     category_of_inpt_ctgry = input(f'{list(item.keys())}, What category you want to Scrap').title()
#     # response = requests.get(f'{wburl}{item[category_of_inpt_ctgry]}')











