from db.db import db_session
from db.models import Price


def delete_element(data):#Сделать запись в логи
    #Должна запрашивать определенному айди сообщения или клиент айди
    del_data = Price.query.filter(Price.offer_id == data['offer_id']).first()
    db_session.delete(del_data)
    db_session.commit()
