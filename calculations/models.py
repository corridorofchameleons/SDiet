from datetime import datetime
from sqlalchemy import MetaData, Integer, Float, String, DATE, ForeignKey, Table, Column, TIMESTAMP, Boolean

metadata = MetaData()

records = Table(
    'records',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False),
    Column('date', String),
    Column('name', String),
    Column('weight', Float),
    Column('protein', Float),
    Column('fats', Float),
    Column('carbohydrates', Float),
    Column('calories', Float),
)
