from db.del_data import delete_element


def check_prices(prices_finish, prices_start):
    keys = prices_start.keys()
    while True:
        for key in keys:
            if prices_finish[key] != prices_start[key]:
                return make_updated_prices(prices_finish, prices_start)
                break
        return None
        break


def make_updated_prices(prices_finish, prices_start):
    rate = prices_finish['rate']
    update_prices = {
        'offer_id': prices_start['offer_id'],
        'price': str(compare(prices_finish['price'], prices_start['price'], rate)),
        'old_price': str(compare(prices_finish['old_price'], prices_start['old_price'],rate)),
        'min_price': str(compare(prices_finish['min_price'], prices_start['min_price'],rate))
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


def check_update_prices(report, prices_finish):
    if report is None:
        delete_element(prices_finish)#Можно записать в логи
    


def get_updated_prices(prices_finish, prices_start):
    updated_prices = check_prices(prices_finish, prices_start)
    check_update_prices(updated_prices, prices_finish)
    return updated_prices


if __name__ == '__main__':
    data = 'G0023;573;828;486'

    data_1 = {
        'offer_id': 'G0023',
        'price': '700',
        'old_price': '825',
        'min_price': '435',
        'rate': 2,
    }
    data_2 = {
        'offer_id': 'G0023',
        'price': '573',
        'old_price': '828',
        'min_price': '487'
    }

    print(get_updated_prices(data_1, data_2))
