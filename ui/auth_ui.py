import tkinter as tk
from tkinter import ttk
from logic.auth import authenticate_user
from logic.employee import handle_employee
from logic.customer import handle_customer

def open_auth_window():
    # Функция для авторизации
    def login():
        username = entry_username.get()
        password = entry_password.get()
        selected_role = role_combobox.get()  # Получаем выбранную роль из ComboBox

        # Проверка роли и логина/пароля
        if selected_role == "Продавец":
            role = authenticate_user("Seller", username, password)
        elif selected_role == "Покупатель":
            role = authenticate_user("Customer", username, password)
        else:
            label_error.config(text="Выберите роль!")
            return

        if role:
            print(f"Успешный вход! Роль: {role}")
            if role == 'Seller':
                handle_employee()  # Вызов логики для продавца
                open_employee_window()  # Открытие окна для продавца
            elif role == 'Customer':
                handle_customer()  # Вызов логики для покупателя
                open_customer_window()  # Открытие окна для покупателя
            root.destroy()  # Закрываем окно авторизации после входа
        else:
            label_error.config(text="Неверный логин или пароль!")

    # Создаем основное окно
    root = tk.Tk()
    root.title("Авторизация")
    root.geometry("400x250")

    # Поле для логина
    tk.Label(root, text="Логин").grid(row=0, column=0)
    entry_username = tk.Entry(root)
    entry_username.grid(row=0, column=1)

    # Поле для пароля
    tk.Label(root, text="Пароль").grid(row=1, column=0)
    entry_password = tk.Entry(root, show="*")
    entry_password.grid(row=1, column=1)

    # Выбор роли с помощью ComboBox
    tk.Label(root, text="Выберите роль").grid(row=2, column=0)

    # Создаем комбобокс для выбора роли
    role_combobox = ttk.Combobox(root, values=["Продавец", "Покупатель"])
    role_combobox.set("Продавец")  # По умолчанию роль - продавец
    role_combobox.grid(row=2, column=1)

    # Кнопка для входа
    button_login = tk.Button(root, text="Войти", command=login)
    button_login.grid(row=3, column=0, columnspan=2)

    # Место для отображения ошибок
    label_error = tk.Label(root, text="", fg="red")
    label_error.grid(row=4, column=0, columnspan=2)

    root.mainloop()
