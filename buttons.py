from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton,\
                          ReplyKeyboardMarkup, KeyboardButton


# Кнопки со всеми продуктами(основное меню)
def main_menu(get_pr_name_id):
    #  Создаем пространство для кнопок
    buttons = InlineKeyboardMarkup(row_width=2)

    # Создать кнопки (незгораемые кнопки)
    order = InlineKeyboardButton(text="Оформить заказ", callback_data='order')
    cart = InlineKeyboardButton(text="Корзина", callback_data='cart')

    # Генерация кнопок с товарами(Базы данных)
    all_products = [InlineKeyboardButton(text=f"{i[0]}", callback_data=i[1]) for i in get_pr_name_id]
    print(all_products)

    # Обьединить наши кнопки с пространством
    buttons.row(order)
    buttons.add(*all_products)
    buttons.row(cart)

    return buttons


# Кнопки для выбора кол-во
def choose_product_count(plus_or_minus='', current_amount=1):
    # Создать пространсво
    buttons = InlineKeyboardMarkup(row_width=3)

    # Несгораемые кнопки
    back = InlineKeyboardButton(text='Назад', callback_data='back')
    plus = InlineKeyboardButton(text='+', callback_data='plus')
    minus = InlineKeyboardButton(text='-', callback_data='minus')
    count = InlineKeyboardButton(text=str(current_amount), callback_data=str(current_amount))
    cart = InlineKeyboardButton(text='Добавить в корзину', callback_data='to_cart')

    # Отслеживать плюс или минус
    if plus_or_minus == 'plus':
        new_amount = int(current_amount) + 1
        count = InlineKeyboardButton(text=str(new_amount), callback_data=str(new_amount))
    elif plus_or_minus == 'minus':
        if int(current_amount) > 1:
            new_amount = int(current_amount) - 1
            count = InlineKeyboardButton(text=str(new_amount), callback_data=str(new_amount))

    buttons.add(minus, count, plus)
    buttons.row(cart)
    buttons.row(back)

    return buttons


def number_buttons():
    buttons = ReplyKeyboardMarkup(resize_keyboard=True)
    num_buttons = KeyboardButton('Поделиться контактом', request_contact=True)

    buttons.add(num_buttons)

    return buttons