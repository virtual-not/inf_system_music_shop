import tkinter as tk
from tkinter import messagebox
from database.db_connection import get_connection
from database.queries import ADD_PRODUCT

def handle_employee():
    # Логика для сотрудника (продавца)
    print("Продавец авторизовался, можно продолжить работу.")

    # Окно для добавления товара
    employee_window = tk.Tk()
    employee_window.title("Добавление товара")
    employee_window.geometry("400x350")

    tk.Label(employee_window, text="Добавьте новый товар:").pack()

    # Ввод названия товара
    tk.Label(employee_window, text="Название товара:").pack()
    entry_name = tk.Entry(employee_window)
    entry_name.pack()

    # Ввод бренда товара
    tk.Label(employee_window, text="Бренд товара:").pack()
    entry_brand = tk.Entry(employee_window)
    entry_brand.pack()

    # Ввод жанра товара
    tk.Label(employee_window, text="Жанр товара (опционально):").pack()
    entry_genre = tk.Entry(employee_window)
    entry_genre.pack()

    # Ввод класса инструмента
    tk.Label(employee_window, text="Класс инструмента:").pack()
    entry_class = tk.Entry(employee_window)
    entry_class.pack()

    # Ввод цены товара
    tk.Label(employee_window, text="Цена товара:").pack()
    entry_price = tk.Entry(employee_window)
    entry_price.pack()

    # Ввод количества товара на складе
    tk.Label(employee_window, text="Количество на складе:").pack()
    entry_quantity = tk.Entry(employee_window)
    entry_quantity.pack()

    # Функция для добавления товара в БД
    def add_product():
        name = entry_name.get()
        brand = entry_brand.get()
        genre = entry_genre.get() if entry_genre.get() else None  # Опциональное поле
        instrument_class = entry_class.get()
        price = entry_price.get()
        quantity = entry_quantity.get()

        if not name or not brand or not instrument_class or not price or not quantity:
            messagebox.showerror("Ошибка", "Все обязательные поля должны быть заполнены!")
            return

        # Проверка, что цена и количество - это числа
        try:
            price = float(price)
            quantity = int(quantity)
        except ValueError:
            messagebox.showerror("Ошибка", "Цена и количество должны быть числами!")
            return

        if price <= 0 or quantity < 0:
            messagebox.showerror("Ошибка", "Цена должна быть больше нуля, а количество не может быть отрицательным!")
            return

        # Соединение с базой данных
        connection = get_connection()
        cursor = connection.cursor()

        # Выполнение запроса для добавления товара
        cursor.execute(ADD_PRODUCT, (name, brand, genre, instrument_class, price, quantity))
        connection.commit()  # Подтверждаем изменения в БД

        # Очистим поля
        entry_name.delete(0, tk.END)
        entry_brand.delete(0, tk.END)
        entry_genre.delete(0, tk.END)
        entry_class.delete(0, tk.END)
        entry_price.delete(0, tk.END)
        entry_quantity.delete(0, tk.END)

        messagebox.showinfo("Успех", "Товар добавлен в базу данных!")

        # Закрываем соединение с БД
        cursor.close()
        connection.close()

    # Кнопка для добавления товара
    button_add_product = tk.Button(employee_window, text="Добавить товар", command=add_product)
    button_add_product.pack()

    employee_window.mainloop()
