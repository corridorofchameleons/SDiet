from datetime import datetime
from sqlalchemy import MetaData, Integer, Float, String, DATE, ForeignKey, Table, Column, TIMESTAMP, Boolean

metadata = MetaData()

# weights = Table(
#     'weights',
#     metadata,
#     Column('id', Integer, primary_key=True),
#     Column('user', Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False),
#     Column('value', Float, nullable=False),
#     Column('date', DATE, default=datetime.now().date())
# )
#
# records = Table(
#     'records',
#     metadata,
#     Column('id', Integer, primary_key=True),
#     Column('user', Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False),
#     Column('date', DATE, default=datetime.now().date()),
#     Column('product', Integer, ForeignKey('products.id', ondelete='RESTRICT'), nullable=False),
#     Column('amount', Float, nullable=False)
# )

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
