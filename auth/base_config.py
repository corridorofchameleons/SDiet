from datetime import datetime

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy import String, Boolean, Column, Integer, TIMESTAMP

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase, Mapped

from database import get_async_session


class Base(DeclarativeBase):
    pass


class Users(SQLAlchemyBaseUserTable[int], Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    email: Mapped[str] = Column(String(length=320), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = Column(String(length=1024), nullable=False)
    is_active: Mapped[bool] = Column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = Column(Boolean, default=False, nullable=False)
    is_verified: Mapped[bool] = Column(Boolean, default=False, nullable=False)


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, Users)
