from sqlalchemy.exc import SQLAlchemyError

from db.db import db_session
from db.models import Chat_number, Price
from db.utils import check_product


def load_data(data, chat_id):
    chat_info = get_or_load_chat_info(chat_id)
    product = check_product(data, chat_info) 
    print(product)
    if product:
        return False
    else:
        responce = load_user_data(data, chat_info)
        return responce


def load_user_data(report, chat_info):#Сделать запись в логи
    data = Price(
        offer_id=report['offer_id'],
        price=report['price'],
        old_price=report['old_price'],
        min_price=report['min_price'],
        rate = report['rate'],
        chat_number_id=chat_info.id,
    )
    db_session.add(data)
    try:
        db_session.commit()
        return True
    except SQLAlchemyError:
        db_session.rollback()
        #Здесь сообщить пользователю
        return False


def get_or_load_chat_info(chat_id):
    chat_info = Chat_number.query.filter(Chat_number.number == chat_id).first()
    if not chat_info:
        chat_info = Chat_number(number=chat_id)
        db_session.add(chat_info)
        try:
            db_session.commit()
        except SQLAlchemyError:
            db_session.rollback()
            #Здесь сообщить пользователю
            raise
        db_session.refresh(chat_info)

    return chat_info
