import sqlite3

def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
        print("Connection successful!")
    except sqlite3.Error as e:
        print(e)
    return connection

def create_table(connection, sql):
        try:
            cursor = connection.cursor()
            cursor.execute(sql)
        except sqlite3.Error as e:
            print(e)


def insert_products(connection, product):
    try:
        sql = '''INSERT INTO products 
        (product_title, prise, quantity) 
        VALUES ( ?, ?, ?)'''
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def update_product_quantity(connection, product_id, new_quantity):
    try:
        sql = '''UPDATE products
                 SET quantity = ?
                 WHERE id = ?'''

        cursor = connection.cursor()
        cursor.execute(sql, (new_quantity, product_id))
        connection.commit()

        print(f"Updated product ID {product_id} with new quantity: {new_quantity}")
    except sqlite3.Error as e:
        print(e)


def update_product_quantity(connection, product_id, new_quantity):
    try:
        sql = '''UPDATE products
                 SET quantity = ?
                 WHERE id = ?'''

        cursor = connection.cursor()
        cursor.execute(sql, (new_quantity, product_id))
        connection.commit()

        print(f"Updated product ID {product_id} with new quantity: {new_quantity}")
    except sqlite3.Error as e:
        print(e)


def update_product_price(connection, product_id, new_price):
    try:
        sql = '''UPDATE products
                 SET price = ?
                 WHERE id = ?'''

        cursor = connection.cursor()
        cursor.execute(sql, (new_price, product_id))
        connection.commit()

        print(f"Updated product ID {product_id} with new price: {new_price}")
    except sqlite3.Error as e:
        print(e)


def delete_product_by_id(connection, product_id):
    try:
        sql = '''DELETE FROM products
                 WHERE id = ?'''

        cursor = connection.cursor()
        cursor.execute(sql, (product_id,))
        connection.commit()

        print(f"Deleted product ID {product_id}")
    except sqlite3.Error as e:
        print(e)


def select_all_products(connection):
    try:
        sql = '''SELECT * FROM products'''

        cursor = connection.cursor()
        cursor.execute(sql)

        products = cursor.fetchall()

        print("Все товары в базе данных:")
        for product in products:
            product_id, product_title, price, quantity = product
            print(f"ID: {product_id}, Название: {product_title}, Цена: {price}, Количество: {quantity}")

    except sqlite3.Error as e:
        print(e)


def select_products_under_price_and_quantity(connection, price_limit, quantity_limit):
    try:
        sql = '''SELECT * FROM products
                 WHERE price < ? AND quantity > ?'''

        cursor = connection.cursor()
        cursor.execute(sql, (price_limit, quantity_limit))

        products = cursor.fetchall()

        print(f"Товары дешевле {price_limit} сомов и с количеством больше {quantity_limit}:")
        for product in products:
            product_id, product_title, price, quantity = product
            print(f"ID: {product_id}, Название: {product_title}, Цена: {price}, Количество: {quantity}")

    except sqlite3.Error as e:
        print(e)


def search_products_by_name(connection, search_term):
    try:
        sql = '''SELECT * FROM products
                 WHERE product_title LIKE ?'''

        cursor = connection.cursor()
        # Добавляем % к поисковому термину для использования LIKE
        cursor.execute(sql, (f"%{search_term}%",))

        products = cursor.fetchall()

        print(f"Товары, содержащие '{search_term}' в названии:")
        for product in products:
            product_id, product_title, price, quantity = product
            print(f"ID: {product_id}, Название: {product_title}, Цена: {price}, Количество: {quantity}")

    except sqlite3.Error as e:
        print(e)


sql_to_create_products_table = '''
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR(200) NOT NULL,
    prise REAL NOT NULL DEFAULT 0.0,
    quantity NOT NULL DEFAULT 0
 )
'''

my_connection = create_connection('''hw.db''')
# create_table(my_connection, sql_to_create_products_table)
print('DONE!')
'''Список из 15 продуктов'''
# insert_products(my_connection, ('Apple Juice', 120, 30))
# insert_products(my_connection, ('Bread', 50, 60))
# insert_products(my_connection, ('Milk', 90, 40))
# insert_products(my_connection, ('Rice', 400, 25))
# insert_products(my_connection, ('Chicken Breast', 550, 20))
# insert_products(my_connection, ('Pasta', 150, 35))
# insert_products(my_connection, ('Cereal', 220, 50))
# insert_products(my_connection, ('Olive Oil', 700, 15))
# insert_products(my_connection, ('Eggs (Dozen)', 120, 45))
# insert_products(my_connection, ('Butter', 250, 30))
# insert_products(my_connection, ('Sugar', 60, 70))
# insert_products(my_connection, ('Coffee', 400, 20))
# insert_products(my_connection, ('Tomato Ketchup', 150, 40))
# insert_products(my_connection, ('Laundry Detergent', 300, 25))
# insert_products(my_connection, ('Toilet Paper (Pack of 4)', 200, 50))
'''  Обновляет количество товара с ID 1 до 50'''
# update_product_quantity(my_connection, 1, 50)

'''Изменяет количество товара с ID 1 на 50'''
# update_product_quantity(my_connection, 1, 50)

'''Изменяет цену товара с ID 2 на 180'''
# update_product_price(my_connection, 2, 180)

'''Удаляет товар с ID 3'''
# delete_product_by_id(my_connection, 3)

''' Извлекает и выводит все товары из таблицы'''
# select_all_products(my_connection)

'''Извлекает и выводит товары, которые дешевле заданного
 лимита по цене и имеют количество больше заданного лимита.'''
# select_products_under_price_and_quantity(my_connection, 100, 5)

''' Выполняет поиск по названию и выводит товары, название
 которых содержит заданное слово или фразу'''
# search_products_by_name(my_connection, 'Butter')

my_connection.close()
