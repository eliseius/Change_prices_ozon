import json
import requests

from constants import URL_UPDATE_PRICES
from settings import OZON_API_KEY, OZON_CLIENT_ID


def make_prices_update(offer_id, price, old_price, min_price):#Сделать запись в логи
    headers = {'Client-Id': OZON_CLIENT_ID, 'Api-Key': OZON_API_KEY,
               'Content-Type': 'application/json'}
    params = {
        'prices':[
            {
                'offer_id': offer_id,
                'price': price,
                'old_price': old_price,
                'min_price': min_price,
            }
        ]
    }

    params = json.dumps(params)
    response = requests.post(URL_UPDATE_PRICES, headers=headers, data=params)
    if response:
        try:
            result = response.json()
            return result
        except ValueError:
            print('Ошибка сформированных данных')
            return None
    else:
        print('Сетевая ошибка')
        print(response.status_code)
    return None


def update_prices(report):
    if report is not None:
        offer_id = report['offer_id']
        price = report['price']
        old_price = report['old_price']
        min_price = report['min_price']
        response_report = make_prices_update(offer_id, price, old_price, min_price)
        if response_report:
            return response_report
