from sqlalchemy import Column, Integer, String
from db.db import Base, engine

class Price (Base):
    __tablename__ = "Change_prices"

    id = Column(Integer(), primary_key=True)
    offer_id = Column(String, unique=True)
    price = Column(String)
    old_price = Column(String)
    min_price = Column(String)
    rate = Column(Integer)

    def __repr__(self):
        return f"Product id: {self.id}, artikul: {self.offer_id}"


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
