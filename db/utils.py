from db.models import Chat_number, Price


def check_product(report, chat_info):
    change_prices = Price.query.filter(Price.chat_number_id == chat_info.id)
    if change_prices.count() != 0:
        for element in change_prices:
            if element.offer_id == report['offer_id']:
                return True
    return False


def get_product(report, chat_id):
    chat_info = Chat_number.query.filter(Chat_number.number == chat_id).first()
    
    for product in Price.query.filter(Price.chat_number_id == chat_info.id):
        if product.offer_id == report['offer_id']:
            return product
    return False
