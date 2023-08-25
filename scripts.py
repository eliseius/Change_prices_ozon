import schedule
import time

from datetime import datetime


from actual_prices import get_actual_prices
from logics import get_updated_prices
from update_prices import update_prices
from utils import process_data






def main(data, rate):
    prices_finish = process_data(data)
    offer_id = prices_finish['offer_id']
    prices_start = get_actual_prices(offer_id)#None??
    send_prices = get_updated_prices(prices_finish, prices_start, rate)
    report = update_prices(send_prices)#None??

def pprint():
    print('Время пришло')


if __name__ == '__main__':
    data = 'G0023;573;828;486'
    rate = 2
    time_start = '00:59:00'

    print(time_start)

    schedule.every().day.at(time_start).do(pprint)
    while True:
        schedule.run_pending()
        time.sleep(1)

   # main(data, rate)
