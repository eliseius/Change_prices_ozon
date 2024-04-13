from db.models import Chat_number, Price
from db.load_data import load_data
from utils import process_data


def get_prices_for_change():#Должна запрашивать определенному айди сообщения или клиент айди
    query = Price.query.all()
   # query = Price.query.filter(Chat_number.number == id_chat).all()

    if query:
        product_prices = []
        for element in query:
            one_product = {
            'offer_id': element.offer_id,
            'price': element.price,
            'old_price': element.old_price,
            'min_price': element.min_price,
            'rate': element.rate,
            }
            product_prices.append(one_product)
        return product_prices
    else:
        return None
  

def get_chat_id():#Заглушка работает только с одним пользователем
    chat_needed = Chat_number.query.first()
    return chat_needed.number


def get_list_chat_id():
    all_chats = Chat_number.query.all()
    all_id_chats = []
    for chat in all_chats:
        all_id_chats.append(chat.number)
    return all_id_chats


if __name__ == '__main__':
    data = 'G0022;573;828;486;2'
    data_raw = data.split(sep=';')
    data_send = process_data(data_raw)
    #print(data_send)
    load_data(data_send, 387757973)
    #get_prices_for_change(387757973)