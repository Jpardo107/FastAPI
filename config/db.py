from sqlalchemy import create_engine, MetaData

engine = create_engine('mysql+pymysql://root:rootrootroot@127.0.0.1:3306/backend')

meta_data = MetaData()