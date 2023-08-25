def get_updated_prices(prices_finish, prices_start, rate):
    update_prices = {
        'offer_id': prices_start['offer_id'],
        'price': str(compare(prices_finish['price'], prices_start['price']), rate),
        'old_price': str(compare(prices_finish['old_price'], prices_start['old_price']),rate),
        'min_price': str(compare(prices_finish['min_price'], prices_start['min_price']),rate)
    }
    return update_prices


def compare(price_finish, price_start, rate):
    price_finish = int(price_finish)
    price_start = int(price_start)
    if price_finish > price_start:
        price = int(round(price_start * (1 + rate / 100), 0))
        if price_finish < price:
            price = price_finish
    elif price_finish < price_start:
        price = int(round(price_start * (1 - rate / 100), 0))
        if price_finish > price:
            price = price_finish
    else:
        price = ''
    return price
