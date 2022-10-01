from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import engine, meta_data

comment = Table('contact', meta_data,
                Column('id', Integer, primary_key=True, nullable=False),
                Column('name', String(60), nullable=False),
                Column('email', String(60), nullable=False),
                Column('comment', String(255), nullable=False)
                )

meta_data.create_all(engine)