from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi_users import FastAPIUsers
from sqlalchemy import select, insert, desc, func
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
async def create_record(record: RecordCreate, session: AsyncSession = Depends(get_async_session),
                        # user: Users = Depends(current_user)
                        ):
    record.user_id = 1
    stmt = insert(records).values(**record.model_dump())
    print(stmt)
    await session.execute(stmt)
    await session.commit()


@router.get('/')
async def get_record(date: str, session: AsyncSession = Depends(get_async_session),
                        # user: Users = Depends(current_user)
                        ):
    user_id = 1
    stmt = select(records).where(records.c.user_id == user_id, records.c.date == date)
    result = await session.execute(stmt)
    res = [{'id': a, 'name': d, 'amt': e, 'protein': round(f, 1), 'fats': round(g, 1), 'carbohydrates': round(h, 1), 'calories': round(i)} for a, b, c, d, e, f, g, h, i in result.all()]
    return res

