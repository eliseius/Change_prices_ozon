from utils import make_keyboard

def greet_users(update, context):
    
    text = 'Обновить цену товара'
    update.message.reply_text(f'Здравствуй! Этот бот умеет обновлять цены товаров OZON.', reply_markup=make_keyboard(text))