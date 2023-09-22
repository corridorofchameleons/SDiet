import json

from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy import select, insert
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
    query = select(categories)
    result = await session.execute(query)
    res = [{'id': a, 'name': b} for a, b in result.all()]
    return res


@router.get('/{cat_id}')
async def get_products(cat_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(products).where(products.c.category == cat_id)
    result = await session.execute(query)
    res = [{'id': a, 'name': b, 'protein': c, 'fats': d, 'carbohydrates': e, 'category': f} for a, b, c, d, e, f in result.all()]
    return res


@router.post('/add_product')
async def get_products(operation: OperationCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(products).values(**operation.model_dump())
    await session.execute(stmt)
    await session.commit()
    return {'status': 'Продукт успешно добавлен'}
