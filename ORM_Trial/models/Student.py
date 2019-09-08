from sqlalchemy import Column, ForeignKey, Integer, String, Table
from . import Base, session


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name=None):
        self.name = name


    @staticmethod
    def get_all():
        return session.query(Student).order_by(Student.name).all()
