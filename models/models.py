from sqlalchemy import MetaData, Integer, Float, String, DATE, ForeignKey, Table, Column
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from config import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME

metadata = MetaData()


categories = Table(
    'categories',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False)
)

products = Table(
    'products',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String, nullable=False),
    Column('protein', Float, nullable=False, default=0.0),
    Column('fats', Float, nullable=False, default=0.0),
    Column('carbohydrates', Float, nullable=False, default=0.0),
    Column('category', Integer, ForeignKey('categories.id', ondelete='RESTRICT'))
)


