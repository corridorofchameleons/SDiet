from datetime import datetime
from sqlalchemy import MetaData, Integer, Float, String, DATE, ForeignKey, Table, Column, TIMESTAMP, Boolean

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
    Column('calories', Float, nullable=True, default=0.0),
    Column('category', Integer, ForeignKey('categories.id', ondelete='RESTRICT'))
)
