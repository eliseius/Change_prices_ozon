from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship

from db.db import Base, engine


# user_store = Table('chat_access', Base.matadata,
#                     Column('chat_number_id', Integer, ForeignKey("chat_numbers.id")),
#                     Column('access_id', Integer, ForeignKey("ozon_accesses.id")),
#                     )


class User_store (Base):
    _tablename_ = "user_store"

    id = Column(Integer(), primary_key=True)
    chat_number_id = Column(Integer, ForeignKey('chat_numbers.id'))
    ozon_access_id = Column(Integer, ForeignKey('ozon_accesse.id'))
    name_store = Column(String(20))


class Chat_number (Base):
    __tablename__ = "chat_numbers"

    id = Column(Integer(), primary_key=True)
    number = Column(Integer, unique=True)
    ozon_accesses = relationship('User_store')

    def __repr__(self):
        return f"Chat id: {self.id}, chat_number: {self.number}"



class Ozon_access (Base):
    __tablename__ = "ozon_accesses"

    id = Column(Integer(), primary_key=True)
    client_id = Column(Integer)
    api_key = Column()
    price = relationship('Price')
    chat_numbers = relationship('User_store')



class Price (Base):
    __tablename__ = "change_prices"

    id = Column(Integer(), primary_key=True)
    offer_id = Column(String)
    price = Column(Integer)
    old_price = Column(Integer)
    min_price = Column(Integer)
    rate = Column(Integer)
    access_id = Column(Integer, ForeignKey('ozon_acces.id'))

    def __repr__(self):
        return f"Product id: {self.id}, artikul: {self.offer_id}"


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
