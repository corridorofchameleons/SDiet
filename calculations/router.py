from typing import List

from fastapi import APIRouter, Depends, Response
from fastapi.encoders import jsonable_encoder
from fastapi_users import FastAPIUsers
from sqlalchemy import select, insert, desc, func, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.testing.pickleable import User

from auth.auth import auth_backend

from auth.manager import get_user_manager
from auth.models import Users

from calculations.models import records
from database import get_async_session
from calculations.schemas import RecordCreate

fastapi_users = FastAPIUsers[Users, int](
    get_user_manager,
    [auth_backend],
)

current_user = fastapi_users.current_user()


router = APIRouter(
    prefix='/records',
    tags=['Records']
)


@router.post('/')
async def create_record(record_list: List[RecordCreate], session: AsyncSession = Depends(get_async_session),
                        user: Users = Depends(current_user)):
    for record in record_list:
        record.user_id = user.id
        stmt = insert(records).values(**record.model_dump())

        await session.execute(stmt)
        await session.commit()


@router.get('/')
async def get_record(date: str, session: AsyncSession = Depends(get_async_session),
                     user: Users = Depends(current_user)):
    print('getting records...')
    user_id = user.id
    stmt = select(records).where(records.c.user_id == user_id, records.c.date == date)
    result = await session.execute(stmt)
    res = [{'id': a, 'name': d, 'amt': e, 'protein': round(f, 1), 'fats': round(g, 1), 'carbohydrates': round(h, 1), 'calories': round(i)} for a, b, c, d, e, f, g, h, i in result.all()]
    return res


@router.delete('/{rec_id}')
async def delete_record(rec_id: int, session: AsyncSession = Depends(get_async_session),
                     user: Users = Depends(current_user)):
    stmt = delete(records).where(records.c.id == rec_id)
    await session.execute(stmt)
    await session.commit()

