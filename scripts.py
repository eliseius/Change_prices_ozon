import schedule
import time

from datetime import datetime

from db.load_data import save_user_data
from logics import get_updated_prices
from requestes.actual_prices import get_actual_prices
from requestes.queries_in_db import get_prices_for_change
from requestes.update_prices import update_prices
from utils import process_data

  
def load_data_in_db(data, rate):
    report = process_data(data)
    report['rate'] = rate
    try:
        save_user_data(report)
    except Exception:#При повторной записи в БД одного и того же  спрашивать у пользователя что делать
        print('Для этого артикла уже есть измения')



def main():
    all_prices= get_prices_for_change()
    if all_prices:
        for one_prices in all_prices:
            offer_id = one_prices['offer_id']
            prices_start = get_actual_prices(offer_id)
            if prices_start:#Если None может запись в логи??
                send_prices = get_updated_prices(one_prices, prices_start)
                if send_prices:
                    update_prices(send_prices) # вернется отчет где можно проверить True
    else:
        print('Нет данных для изменения! БД пуста')


if __name__ == '__main__':
    data = 'G0023;573;828;486'
    rate = 2
    load_data_in_db(data, rate)# Сюда загружать данные из телеграмма

    # time_start = '00:01:00'

    # print(time_start)

    # schedule.every().day.at(time_start).do(main)
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)

