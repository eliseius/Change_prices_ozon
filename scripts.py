import schedule
import time

from logics import get_updated_prices
from requestes.actual_prices import get_actual_prices
from requestes.queries_in_db import get_prices_for_change, get_list_chat_id
from requestes.update_prices import update_prices
from send_message import save_report


def main_script():
    """
    Нужно изменить БД чтобы при старте вводили КЛИЕТН ИД и КЛЮЧ АПИ и они записывались в БД
    И тогда запрос, изменения и сообщения делались только ПРАВИЛЬНОМУ пользователю
    """
    all_prices = get_prices_for_change()
    if all_prices:
        for one_prices in all_prices:
            offer_id = one_prices['offer_id']
            prices_start = get_actual_prices(offer_id)
            if prices_start:#Если None может запись в логи??
                send_prices = get_updated_prices(one_prices, prices_start)
                print(send_prices)
                
                # if send_prices:
                #     save_report(send_prices)
                #     responce = update_prices(send_prices) # вернется отчет где можно проверить True
                #     print(responce)
    else:
        print('Нет данных для изменения! БД пуста')


# def run_update():
#     all_id_chats = get_list_chat_id()
#     for id_chat in all_id_chats:
#         collect_information(id_chat)


# def collect_information(id_chat):
#     all_prices = get_prices_for_change(id_chat)
#     if all_prices:
#         for one_prices in all_prices:




def start_script():
    print('Скрипт запущен')
    #time_start = '00:01:00'# При желании и время старта для каждого пользоателя может быть отдельно настраиваться
    #schedule.every().day.at(time_start).do(main)
    schedule.every(60).seconds.do(main_script)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
   start_script()
