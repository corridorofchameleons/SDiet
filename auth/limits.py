from fastapi import APIRouter, Depends
from fastapi_users import FastAPIUsers
from requests import delete
from sqlalchemy import insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from auth.auth import auth_backend

from auth.manager import get_user_manager
from auth.models import Users
from calculations.models import limits
from calculations.schemas import UpdateLimits
from database import get_async_session

fastapi_users = FastAPIUsers[Users, int](
    get_user_manager,
    [auth_backend],
)

current_user = fastapi_users.current_user()


router = APIRouter(
    prefix='/limits',
    tags=['Limits']
)


@router.post('/')
async def update_limits(data: UpdateLimits, session: AsyncSession = Depends(get_async_session),
                        user: Users = Depends(current_user)):
    data.user_id = user.id

    stmt = select(limits).where(limits.c.user_id == data.user_id)
    result = await session.execute(stmt)
    if not result.all():
        ins_stmt = insert(limits).values(**data.model_dump())
        await session.execute(ins_stmt)
        await session.commit()
    else:
        upd_stmt = update(limits).where(limits.c.user_id == data.user_id).values(**data.model_dump())
        await session.execute(upd_stmt)
        await session.commit()


@router.get('/')
async def get_limits(session: AsyncSession = Depends(get_async_session),
                        user: Users = Depends(current_user)):
    stmt = select(limits).where(limits.c.user_id == user.id)
    result = await session.execute(stmt)
    res = [{"user_id": a, "protein": b, "fats": c, "carbohydrates": d, "calories": e} for a, b, c, d, e in result.all()][0]
    print(res)

    return res


