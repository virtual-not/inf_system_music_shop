import tkinter as tk
from database.db_connection import get_connection
from database.queries import GET_PRODUCTS

def handle_customer():
    # Логика для покупателя
    print("Покупатель авторизовался, можно продолжить покупки.")

    # Соединение с базой данных
    connection = get_connection()
    cursor = connection.cursor()

    # Выполнение запроса для получения списка товаров
    cursor.execute(GET_PRODUCTS)
    products = cursor.fetchall()  # Получаем все товары

    # Окно для покупателя с товаром
    customer_window = tk.Tk()
    customer_window.title("Товары для покупателя")
    customer_window.geometry("400x300")

    tk.Label(customer_window, text="Список доступных товаров:").pack()

    # Отображаем товары в списке
    for product in products:
        product_text = f"{product[0]} - {product[1]} руб."  # product[0] - название, product[1] - цена
        tk.Label(customer_window, text=product_text).pack()

    customer_window.mainloop()

    # Закрываем соединение с БД
    cursor.close()
    connection.close()
