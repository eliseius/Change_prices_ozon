from telegram import ReplyKeyboardMarkup


def process_data(data):
    dict_data = {
        'offer_id': data[0],
        'price': int(float(data[1])),
        'old_price': int(float(data[2])),
        'min_price': int(float(data[3])),
        'rate': int(float(data[4])),
    }
    return dict_data


def output_user_data(data):
    all_inform = []
    for k, v in data.items():
        all_inform.append(f'{k}: {v}')

    return '\n'.join(all_inform)
    

def make_keyboard(text):
    return ReplyKeyboardMarkup([[text]])


def make_keyboard_with_answer(text, update):
    reply_keyboard = [['Да', 'Нет']]
    update.message.reply_text(text, reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
