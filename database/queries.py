# Запрос для аутентификации продавца
AUTHENTICATE_SELLER = """
SELECT id FROM Seller
WHERE name = %s AND contact_info = %s;
"""

# Запрос для аутентификации покупателя
AUTHENTICATE_CUSTOMER = """
SELECT id FROM Customer
WHERE name = %s AND contact_info = %s;
"""

# Запрос для получения всех товаров из таблицы musicalinstrument для покупателя
GET_PRODUCTS = """
SELECT name, price FROM musicalinstrument;
"""

# Запрос для добавления нового товара в таблицу musicalinstrument для продавца
ADD_PRODUCT = """
INSERT INTO MusicalInstrument (name, brand, genre, instrument_class, price, stock_quantity)
VALUES (%s, %s, %s, %s, %s, %s);
"""

