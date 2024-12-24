# Запрос для авторизации пользователя
AUTHENTICATE_USER = """
SELECT role 
FROM Users 
WHERE username = %s AND password = %s;
"""

# Запрос для добавления нового покупателя
INSERT_CUSTOMER = """
INSERT INTO Customer (full_name, phone_number, email, user_id)
VALUES (%s, %s, %s, %s);
"""

# Запрос для добавления нового сотрудника
INSERT_EMPLOYEE = """
INSERT INTO Employee (full_name, position, salary, user_id)
VALUES (%s, %s, %s, %s);
"""

# Запрос для получения информации о пользователе по логину
GET_USER_BY_USERNAME = """
SELECT id, username, password, role 
FROM Users 
WHERE username = %s;
"""

# Запрос для создания нового пользователя (сотрудника или покупателя)
CREATE_USER = """
INSERT INTO Users (username, password, role)
VALUES (%s, %s, %s);
"""
