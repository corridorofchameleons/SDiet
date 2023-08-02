import asyncio
import json

import asyncpg

from config import DB_HOST, DB_PORT, DB_USER, DB_NAME, DB_PASS

with open('data/db.json', 'r') as file:
    data = json.load(file)


# This code is synchronous

async def main():
    connection = await asyncpg.connect(host=DB_HOST, port=DB_PORT, user=DB_USER, database=DB_NAME, password=DB_PASS)

    for cat, items in data.items():
        query_1 = f'''INSERT INTO categories (name) VALUES ('{cat}');'''
        await connection.execute(query_1)
        for item in items:
            if "'" in item['name']:
                item['name'] = item['name'].replace("'", "")
            query_2 = f'''INSERT INTO products (name, protein, fats, carbohydrates, category) VALUES ('{item["name"]}', {item["protein"]}, {item["fats"]}, {item["carbohydrates"]}, (SELECT id FROM categories WHERE name = '{cat}'));'''
            await connection.execute(query_2)
        print(f'Finished with category {cat}')

asyncio.run(main())
