import json
import math

from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy import select, insert, desc, func
from sqlalchemy.ext.asyncio import AsyncSession

from products.models import categories, products
from database import get_async_session
from products.schemas import OperationCreate

router = APIRouter(
    prefix='/products',
    tags=['Products']
)


@router.get('/')
async def get_cats(session: AsyncSession = Depends(get_async_session)):
    query = select(categories).where(categories.c.id != 99).order_by(categories.c.name)
    result = await session.execute(query)
    res = [{'id': a, 'name': b} for a, b in result.all()]
    return res


@router.get('/{cat_id}')
async def get_products(cat_id: int, sort: str | None = None, search: str | None = '', page: int = 0, session: AsyncSession = Depends(get_async_session)):
    paginate_by = 30
    stmt = select(products).where(products.c.category == cat_id).filter(func.lower(products.c.name).like(f'%{search}%'))
    if sort:
        print(sort)
        sort_by, order = sort.split('-')
        print(sort_by, order)
        if order == 'asc':
            stmt = stmt.order_by(sort_by)
        elif order == 'desc':
            stmt = stmt.order_by(desc(sort_by))

    result = await session.execute(stmt)

    res = [{'id': a, 'name': b, 'protein': c, 'fats': d, 'carbohydrates': e, 'calories': f, 'category': g} for a, b, c, d, e, f, g in result.all()]

    pages = [i for i in range(math.ceil(len(res) / paginate_by))]
    output = [{'pages': pages}, {'products': res[page*paginate_by:page*paginate_by + paginate_by]}]

    return output


@router.post('/add_product', status_code=201)
async def get_products(operation: OperationCreate, session: AsyncSession = Depends(get_async_session)):
    print(operation.model_dump())
    stmt = insert(products).values(**operation.model_dump())
    await session.execute(stmt)
    await session.commit()
    return {'status': 'Продукт успешно добавлен'}

