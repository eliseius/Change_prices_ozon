import json
import os
import requests

from constants import URL_UPDATE_PRICES


def make_price_update(offer_id, price, old_price, min_price):
    headers = {'Client-Id': os.environ['OZON_CLIENT_ID'], 'Api-Key': os.environ['OZON_API_KEY'],
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
    else:
        print('Сетевая ошибка')
        print(response.status_code)
    return None


def update_prices(report):
    offer_id = report['offer_id']
    price = report['price']
    old_price = report['old_price']
    min_price = report['min_price']
    response_report = make_price_update(offer_id, price, old_price, min_price)
    return response_report
