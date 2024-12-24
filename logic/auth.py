from database.db_connection import get_connection
from database.queries import AUTHENTICATE_SELLER, AUTHENTICATE_CUSTOMER


def authenticate_user(role, username, password):
    conn = get_connection()
    if conn:
        cursor = conn.cursor()

        if role == "Seller":
            cursor.execute(AUTHENTICATE_SELLER, (username, password))
        elif role == "Customer":
            cursor.execute(AUTHENTICATE_CUSTOMER, (username, password))
        else:
            conn.close()
            return None

        result = cursor.fetchone()
        conn.close()
        if result:
            return role  # Роль будет 'Seller' или 'Customer'
        else:
            return None  # Неверные данные
