import json
import os
import requests

from constants import URL_INFO_PRICES


def get_price_raw(offer_id):
    headers = {'Client-Id': os.environ['OZON_CLIENT_ID'], 'Api-Key': os.environ['OZON_API_KEY'],
               'Content-Type': 'application/json'}

    params = {
        "filter": {
            "offer_id": offer_id
        },
        "limit": 100
    }

    params = json.dumps(params)
    response = requests.post(URL_INFO_PRICES, headers=headers, data=params)
    if response:
        try:
            report = response.json()
            return report
        except ValueError:
            print('Ошибка сформированных данных')
    else:
        print('Сетевая ошибка')
        print(response.status_code)
    return None


def short_report(report):
    info_product = report['result']['items'][0]
    prices = info_product['price']
    short_report = {
        'offer_id': info_product['offer_id'],
        'price': prices['price'],
        'old_price': prices['old_price'],
        'min_price': prices['min_price']
    }
    return short_report


def get_actual_prices(offer_id):
    report = get_price_raw(offer_id)
    short_report = short_report(report)
    return short_report
