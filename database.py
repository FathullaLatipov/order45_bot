import sqlite3

from datetime import datetime

db = sqlite3.connect('dostavka.db')

fake_evos = db.cursor()

# Создаем таблицу пользователя
fake_evos.execute('CREATE TABLE IF NOT EXISTS users (tg_id INTEGER, name TEXT,'
                  'phone_number TEXT, address TEXT, reg_date DATETIME);')

# Создаем таблицу продукта
fake_evos.execute('CREATE TABLE IF NOT EXISTS products (pr_id INTEGER PRIMARY KEY AUTOINCREMENT, pr_name TEXT,'
                  'pr_price REAL, pr_quantity INTEGER, pr_des TEXT, pr_photo TEXT, reg_date DATETIME);')

# Создаем таблицу корзины пользователя
fake_evos.execute('CREATE TABLE IF NOT EXISTS user_cart (user_id INTEGER, user_product TEXT,'
                  'quantity INTEGER, total_for_price REAL);')

# Регистрация пользователя
def register_user(tg_id, name, phone_number, address):
    db = sqlite3.connect('dostavka.db')

    fake_evos = db.cursor()

    #Добавления пользователя в базу
    fake_evos.execute('INSERT INTO users (tg_id, name, phone_number, address, reg_date) VALUES '
                      '(?, ?, ?, ?, ?);', (tg_id, name, phone_number, address, datetime.now()))

    db.commit()

# Проверка пользователя через id
def check_user(tg_id):
    db = sqlite3.connect('dostavka.db')

    fake_evos = db.cursor()

    checker = fake_evos.execute('SELECT tg_id FROM users WHERE tg_id=?;', (tg_id,))

    if checker.fetchone():
        return True
    else:
        return False

# Добавления продукта в таблицу
def add_product(pr_name, pr_price, pr_quantity, pr_des, pr_photo):
    db = sqlite3.connect('dostavka.db')

    fake_evos = db.cursor()

    fake_evos.execute('INSERT INTO products (pr_name, pr_price, pr_quantity, pr_des, pr_photo, reg_date) VALUES'
                      '(?, ?, ?, ?, ?, ?);', (pr_name, pr_price, pr_quantity, pr_des, pr_photo, datetime.now()))

    db.commit()

# Получаем все продукты из базы только его (name, pr_id)
def get_pr_name_id():
    db = sqlite3.connect("dostavka.db")

    fake_evos = db.cursor()

    products = fake_evos.execute("SELECT pr_id, pr_name, pr_quantity FROM products;").fetchall()

    sorted_products = [(i[1], i[0]) for i in products if i[2] > 0]

    return sorted_products

# Получить информацию про определенный продукт через его pr_id
def get_product_info_id(pr_id):
    db = sqlite3.connect('dostavka.db')

    fake_evos = db.cursor()

    product_id = fake_evos.execute('SELECT * FROM products WHERE pr_id=?;', (pr_id,)).fetchone()

    return product_id

# Добавления продуктов в корзину
def add_product_cart(user_id, user_product, quantity):
    db = sqlite3.connect('dostavka.db')

    fake_evos = db.cursor()

    product_price = get_pr_name_id(user_product)

    fake_evos.execute('INSERT INTO user_cart (user_id, user_product, quantity, total_for_price)'
                      'VALUES  (?,?,?,?);', (user_id, user_product, quantity, quantity * product_price))

    db.commit()

# Удаления продуктов из корзины
def delete_product_from_cart(user_id):
    db = sqlite3.connect('dostavka.db')

    fake_evos = db.cursor()

    fake_evos.execute('DELETE FROM user_cart WHERE user_id=?;', (user_id,))


# Получить корзину пользователя
# def get_exact_user_cart(user_id):
#     db = sqlite3.connect('dostavka.db')
#
#     fake_evos = db.cursor()
#
#     user_cart = fake_evos.execute('SELECT products.pr_name, user_cart.quantity, user_cart.total_for_price'
#                                   'FROM products WHERE products.pr_id = user_cart.user_product')
