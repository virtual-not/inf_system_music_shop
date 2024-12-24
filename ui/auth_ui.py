import tkinter as tk
from tkinter import ttk
from logic.auth import authenticate_user

def open_auth_window():
    # Функция для авторизации
    def login():
        username = entry_username.get()
        password = entry_password.get()
        selected_role = role_combobox.get()  # Получаем выбранную роль из комбобокса

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
                open_employee_window()  # Открытие окна для продавца
            elif role == 'Customer':
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

    # Выбор роли с помощью комбобокса
    tk.Label(root, text="Выберите роль").grid(row=2, column=0)

    # Создаем комбобокс для выбора роли
    role_combobox = ttk.Combobox(root, values=["Продавец", "Покупатель"], state="readonly")
    role_combobox.set("Продавец")  # Устанавливаем роль по умолчанию
    role_combobox.grid(row=2, column=1)

    # Кнопка для входа
    button_login = tk.Button(root, text="Войти", command=login)
    button_login.grid(row=4, column=0, columnspan=2)

    # Место для отображения ошибок
    label_error = tk.Label(root, text="", fg="red")
    label_error.grid(row=5, column=0, columnspan=2)

    root.mainloop()

# Окна для продавца и покупателя
def open_employee_window():
    employee_window = tk.Tk()
    employee_window.title("Окно продавца")
    employee_window.geometry("300x200")

    tk.Label(employee_window, text="Добро пожаловать, продавец!").pack()

    employee_window.mainloop()


def open_customer_window():
    customer_window = tk.Tk()
    customer_window.title("Окно покупателя")
    customer_window.geometry("300x200")

    tk.Label(customer_window, text="Добро пожаловать, покупатель!").pack()

    customer_window.mainloop()
