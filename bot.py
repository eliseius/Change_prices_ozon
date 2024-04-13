import logging

from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)

from anketa import prices_start, prices_data, talk_dontunderstend, check_responce, check_question_update
from handlers import greet_users
from settings import API_KEY


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO, filename='bot.log') # Добавить дату и время


def main_bot():
    """
    Нужно изменить БД чтобы при старте вводили КЛИЕТН ИД и КЛЮЧ АПИ и они записывались в БД
    Если клиент уже заполнил секретные данные, то спрашивать их не надо
    И тогда запрос, изменения и сообщения делались только ПРАВИЛЬНОМУ пользователю
    """

    print('Бот запущен')

    mybot = Updater(API_KEY, use_context=True)

    dp = mybot.dispatcher

    prices = ConversationHandler(
        entry_points=[
            MessageHandler(Filters.regex('^(Обновить цену товара)$'), prices_start)
        ],
        states={
            'data': [MessageHandler(Filters.text, prices_data)],
            'responce': [MessageHandler(Filters.text, check_responce)],
            'update':[MessageHandler(Filters.regex('^(Да|Нет)$'), check_question_update)],
        },
        fallbacks=[
          MessageHandler(Filters.text, talk_dontunderstend)
        ]
    )
    dp.add_handler(prices)
    dp.add_handler(CommandHandler('start', greet_users))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main_bot()
