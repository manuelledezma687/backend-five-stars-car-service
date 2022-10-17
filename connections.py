
# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# DATABASE_URL = "mysql+mysqlconnector://root:password@0.0.0.0:5000/fivestars"

# engine = create_engine(DATABASE_URL)

# SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

# Base = declarative_base()

from curses import meta
from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+mysqlconnector://admin:password@localhost:3306/fivestars"")

meta_data = MetaData()
