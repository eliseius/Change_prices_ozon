import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session


engine = create_engine('postgresq+psycopg2://vgbpanoq:7cUQMmHVRHdCUCMI5PJcnrjxZvVwQls@snuffleupagus.db.elephantsql.com:5432/vgbpanoq')#os.environ['DB_POSTGRESQL']) 
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()
