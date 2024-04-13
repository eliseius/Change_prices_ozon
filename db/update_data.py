from sqlalchemy.exc import SQLAlchemyError

from db.db import db_session
from db.load_data import load_user_data
from db.utils import get_product


def update_data(data, chat_id):
    product = get_product(data, chat_id)
    if product:
        responce = update_element(product, data)
    else:
        responce = load_user_data(data, chat_id)
    return responce


def update_element(product, data):
        #Сделать запись в логи
    product.offer_id = data['offer_id']
    product.price = data['price']
    product.old_price = data['old_price']
    product.min_price = data['min_price']
    product.rate = data['rate']
    db_session.add(product)
    try:
        db_session.commit()
        return True
    except SQLAlchemyError:
        db_session.rollback()
        #Здесь сообщить пользователю
        return False
   
