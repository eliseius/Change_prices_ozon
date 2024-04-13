from telegram import ParseMode, ReplyKeyboardRemove
from telegram.ext import ConversationHandler

from db.load_data import load_data
from db.update_data import update_data
from utils import make_keyboard, process_data, output_user_data, make_keyboard_with_answer


def prices_start(update, context):
    update.message.reply_text(
        'Пожалуйста, введите все необходимые данные',
        reply_markup=ReplyKeyboardRemove()
    )
    return 'data'


def prices_data(update, context):
    data = update.message.text
    data_raw = data.split(sep=';')
    if len(data_raw) < 5 or len(data_raw) > 5:
        update.message.reply_text('Не правильный формат данных')
        return 'data'
    else:
        try:
            data_dict = process_data(data_raw)
        except:
            update.message.reply_text('Не правильный формат данных')
            return 'data'
    context.user_data['prices'] = {'data': data_dict}
    chat_id = update.message.chat_id
    context.user_data['prices']['chat_id'] = chat_id
    return check_inform(update, context)


def check_inform(update, context):
    data = context.user_data['prices']['data']
    update.message.reply_text(output_user_data(data), parse_mode = ParseMode.HTML)
    make_keyboard_with_answer('Информация верна?', update)
    return 'responce'


def check_responce(update, context):
    responce = update.message.text
    if responce == 'Да':
        return send_user_data_in_db(update, context)
    elif responce == 'Нет':
        return prices_start(update, context)
    else:
        update.message.reply_text('Я вас не понимаю, ответьте Да или Нет')
        return check_responce(update, context)

    
def send_user_data_in_db(update, context):
    data = context.user_data['prices']['data']
    chat_id = context.user_data['prices']['chat_id']
    responce = load_data(data, chat_id)
    if responce:
        update.message.reply_text('Данные успешно записаны', reply_markup=ReplyKeyboardRemove())
        return conver_end(update, context)
    else:
        make_keyboard_with_answer('Для этого артикла уже есть измения. Хотите поменять?', update)
        return 'update'


def check_question_update(update, context):
    responce = update.message.text
    if responce == 'Да':
        return update_data_in_db(update, context)
    elif responce == 'Нет':
        return conver_end(update, context)


def update_data_in_db(update, context):
    data = context.user_data['prices']['data']
    chat_id = context.user_data['prices']['chat_id']
    responce = update_data(data, chat_id)
    if responce:
        update.message.reply_text('Данные успешно записаны', reply_markup=ReplyKeyboardRemove())
    else:
        update.message.reply_text('Данные не обновлены.Ошибка!! Попробуйте позже')# Заглушка

        pass

    return conver_end(update, context)


def conver_end(update, context):
    text_keyboard = 'Обновить цену товара'
    update.message.reply_text('Добавьте ещё товар для изменения цены', reply_markup=make_keyboard(text_keyboard))
    return ConversationHandler.END




def talk_dontunderstend(update, context):#################
    update.message.reply_text('Я вас не понимаю. Не правильный ответ или введенные данные.')
    text_keyboard = 'Да'
    make_keyboard(text_keyboard)
    return restart(update, context)


def restart(update, context):
    responce = update.message.text
    if responce == 'Да':
        return prices_start(update, context)
    else:
        return ConversationHandler.END


