import tkinter as tk
from ui.auth_ui import open_auth_window

def open_main_window():
    root = tk.Tk()
    root.title("Основное окно")
    root.geometry("300x200")

    tk.Label(root, text="Добро пожаловать в систему!").pack()

    # Кнопка для авторизации
    button_login = tk.Button(root, text="Авторизация", command=open_auth_window)
    button_login.pack()

    root.mainloop()

if __name__ == "__main__":
    open_main_window()