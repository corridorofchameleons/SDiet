from datetime import datetime

from sqlalchemy import MetaData, Integer, Float, String, DATE, ForeignKey, Table, Column, TIMESTAMP, Boolean

metadata = MetaData()

users = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('username', String, nullable=False),
    Column('registered_at', TIMESTAMP, default=datetime.utcnow),
    Column('email', String(length=320), unique=True, index=True, nullable=False),
    Column('hashed_password', String(length=1024), nullable=False),
    Column('is_active', Boolean, default=True, nullable=False),
    Column('is_superuser', Boolean, default=False, nullable=False),
    Column('is_verified', Boolean, default=False, nullable=False),
)


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


