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
