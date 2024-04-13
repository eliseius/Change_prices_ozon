import json
import requests

from constants import URL_INFO_PRICES
from settings import OZON_API_KEY, OZON_CLIENT_ID


def get_price_raw(offer_id):
    headers = {'Client-Id': OZON_CLIENT_ID, 'Api-Key': OZON_API_KEY,
               'Content-Type': 'application/json'}

    params = {
        "filter": {
            "offer_id": [offer_id],
        },
        "limit": 100,
    }

    params = json.dumps(params)
    response = requests.post(URL_INFO_PRICES, headers=headers, data=params)
    if response:
        try:
            report = response.json()
            return report
        except ValueError:
            print('Ошибка сформированных данных')
            return None
    else:
        print('Сетевая ошибка')
        print(response.status_code)
        return None


def make_short_report(report):
    info_product = report['result']['items'][0]
    prices = info_product['price']
    short_report = {
        'offer_id': info_product['offer_id'],
        'price': int(float(prices['price'])),
        'old_price': int(float(prices['old_price'])),
        'min_price': int(float(prices['min_price'])),
    }
    return short_report


def get_actual_prices(offer_id):
    report = get_price_raw(offer_id)
    if report:
        short_report = make_short_report(report)
        return short_report
    else:
        return None
