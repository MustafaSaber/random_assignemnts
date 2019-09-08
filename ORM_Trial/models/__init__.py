from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///db/student.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

from ORM_Trial.models.Student import Student

# Create new tables
Base.metadata.create_all(engine)
