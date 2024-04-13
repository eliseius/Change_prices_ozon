import os
import requests

from pathlib import Path

from requestes.queries_in_db import get_chat_id#Заглушка работает только с одним пользователем
from settings import API_KEY, OZON_CLIENT_ID, NAME_FILE
from utils import process_data


"""
Нужно изменить БД чтобы при старте вводили КЛИЕТН ИД и КЛЮЧ АПИ и они записывались в БД
И тогда запрос, изменения и сообщения делались только ПРАВИЛЬНОМУ пользователю
"""

def save_report(data):
    for k, v in data.items():
        with open(get_path_to_file(), 'a', encoding='utf-8') as file:
            file.write(f'\n{k}: {v}')


def save_text(text):
    with open(get_path_to_file(), 'a', encoding='utf-8') as file:
        file.write(f'\n{text}')



def send_message_for_user():#Отправить тихое сообщение
    message = output_message()
    chat_id = get_chat_id()#Заглушка работает только с одним пользователем
    url = f'https://api.telegram.org/bot{API_KEY}/sendMessage?chat_id={chat_id}&text={message}'
    os.remove(get_path_to_file())
    return requests.get(url).json()


def output_message():#Надо седлать, чтобы прочитать файл построчно
    with open(get_path_to_file(), 'r', encoding='utf-8') as file:
        text = file.read()
    print(text)
    return text
    

def check_message():
    print('Запуск сообщений')
    while True:
        if os.path.exists(get_path_to_file()):
            send_message_for_user()


def get_path_to_file():
    name_file = F'{OZON_CLIENT_ID}-{NAME_FILE}.txt'
    path = Path('messages', name_file)
    return path


if __name__ == '__main__':

    data = 'G0023;573;828;486;2'
    data_raw = data.split(sep=';')
    data_send = process_data(data_raw)
    save_report(data_send)
    text = "Важная запись информации"
    save_text(text)
    print(output_message())