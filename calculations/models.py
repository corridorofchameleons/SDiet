from sqlalchemy import MetaData, Integer, Float, String, ForeignKey, Table, Column

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

limits = Table(
    'limits',
    metadata,
    Column('user_id', Integer, ForeignKey('users.id', ondelete='CASCADE')),
    Column('protein', Float, nullable=True),
    Column('fats', Float, nullable=True),
    Column('carbohydrates', Float, nullable=True),
    Column('calories', Float, nullable=True)
)
