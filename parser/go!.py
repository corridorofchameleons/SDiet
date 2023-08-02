import asyncio
import json
import time

import lxml
from aiohttp import ClientSession
from bs4 import BeautifulSoup
import aiohttp


with open('data/all_categories_dict.json') as file:
    all_categories = json.load(file)

data = {}


async def get_src(session: ClientSession, url: str):
    async with session.get(url) as result:
        html = await result.text()
        return html


async def fetch_data(cat_name, cat_href):
    rep = [',', ' ', '-']
    for sym in rep:
        if sym in cat_name:
            cat_name = cat_name.replace(sym, '_')

    data[cat_name] = []

    p = 0
    has_next_pages = True

    while has_next_pages:

        async with aiohttp.ClientSession() as session:
            print(f'Fetching {cat_href} page {p}...')
            start = time.time()
            src = await get_src(session, url=f'{cat_href}?page={p}')
            print(f'Finished fetching {cat_href} page {p} in {time.time() - start}')

        with open(f'temp/{p}_{cat_name}.html', 'w') as file:
            file.write(src)

        with open(f'temp/{p}_{cat_name}.html') as file:
            src = file.read()

        soup = BeautifulSoup(src, 'lxml')
        try:
            table = soup.find('tbody').find_all(class_='views-field views-field-title active')
        except AttributeError:
            print(f'Failed to fetch table from {cat_name} {cat_href}')
        if soup.find(class_='fa fa-chevron-right') is None:
            has_next_pages = False

        for row in table:
            try:
                temp_data = dict()
                temp_data['name'] = row.text.strip()
                try:
                    temp_data['protein'] = float(row.findNext(class_='views-field views-field-field-protein-value').text)
                except ValueError:
                    temp_data['protein'] = 0.0
                try:
                    temp_data['fats'] = float(row.findNext(class_='views-field views-field-field-fat-value').text)
                except ValueError:
                    temp_data['fats'] = 0.0
                try:
                    temp_data['carbohydrates'] = float(row.findNext(class_='views-field views-field-field-carbohydrate-value').text)
                except ValueError:
                    temp_data['carbohydrates'] = 0.0
                data[cat_name].append(temp_data)
            except:
                print(f'Failed to fetch {row}, setting 0.0')

        p += 1


async def main():
    start = time.time()
    gr = asyncio.gather(*[fetch_data(cn, ch) for cn, ch in all_categories.items()])
    await gr
    print(f'Finished in {time.time() - start}')
    with open(f'data/db.json', 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

asyncio.run(main())
