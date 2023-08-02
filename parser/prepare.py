import requests
from bs4 import BeautifulSoup
import json

url = 'https://calorizator.ru/product'

headers = {
    "accept": "*/*",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 YaBrowser/23.3.3.706 Yowser/2.5 Safari/537.36"
}
req = requests.get(url, headers=headers)
src = req.text

with open('temp/index.html', 'w') as file:
    file.write(src)

with open('temp/index.html', 'r') as file:
    src = file.read()

domain = 'https://calorizator.ru/'
soup = BeautifulSoup(src, 'lxml')
cat_hrefs = soup.find_all(class_='product')
all_hrefs = {}

for group in cat_hrefs:
    for prod in group.findChildren('a'):
        prod_text = prod.text
        prod_href = domain + prod.get('href')
        all_hrefs[prod_text] = prod_href

del all_hrefs['Полный список продуктов']
del all_hrefs['Подбор продуктов']
del all_hrefs['Все продукты в картинках']
del all_hrefs['Производители продуктов']
del all_hrefs['Личный кабинет']

with open('data/all_categories_dict.json', 'w') as file:
    json.dump(all_hrefs, file, indent=4, ensure_ascii=False)



