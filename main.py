import telebot
import database

bot = telebot.TeleBot('6826049560:AAFkjjtK3nw7ESZzycS5LdD_lnl8TrH55bY')


@bot.message_handler(commands=['start'])
def start_message(message):
    user_id = message.from_user.id
    # Проверка пользователя
    checker = database.check_user(user_id)

    #Если пользователь есть в базе
    if checker:
        #Мы должны получить актульный список продуктов
        products = database.get_pr_name_id()
        print(products)

        bot.send_message(user_id, 'Привет')
        # тут у нас будет кнопка на след уроке
        bot.send_message(user_id, 'Выберите пункт меню')
    elif not checker:
        bot.send_message(user_id, 'Привет отправьте свое имя')
        bot.register_next_step_handler(message, get_name)

# Этап получении имени
def get_name(message):
    user_id = message.from_user.id

    #сохраняем пользователя в переменную
    username = message.text

    # тут у нас будет кнопка на след уроке
    bot.send_message(user_id, 'Отправьте номер телефона')
    bot.register_next_step_handler(message, get_number, username)

# Этап получения номера пользователя
def get_number(message, username):
    user_id = message.from_user.id

    # если нам пришел какой то контакт то->
    if message.contact:
        # Сохраняем контакт в временной переменной
        phone_number = message.contact.phone_number

        # Сохраняем пользователя уже в базу
        database.register_user(user_id, username, phone_number, 'Not yet')
        # Тут у нас будет кнопка на след уроке
        bot.send_message(user_id, f'Вы успешно зарегались {username}', )
    # Если пользователь не отправил контакт или написал в текстовом формате
    elif not message.contact:
        # Тут у нас будет кнопка на след уроке
        bot.send_message(user_id, 'Отправьте контакт с помощью кнопки')
        bot.register_next_step_handler(message, get_number, username)







bot.infinity_polling()