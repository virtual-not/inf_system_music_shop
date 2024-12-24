import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
from logic.customer import handle_customer

class TestHandleCustomer(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)  # Патчим sys.stdout для перехвата вывода в консоль
    @patch('database.db_connection.get_connection')
    @patch('tkinter.Tk')  # Мокаем Tkinter
    def test_handle_customer_success(self, MockTk, mock_get_connection, mock_stdout):
        # Мокаем базу данных
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_get_connection.return_value = mock_conn
        mock_cursor.fetchall.return_value = [('Product1', 100), ('Product2', 200)]  # Товары для теста

        # Мокаем создание окна Tkinter
        mock_window = MagicMock()
        MockTk.return_value = mock_window

        # Вызываем функцию
        handle_customer()

        # Проверяем, что покупатель авторизовался
        output = mock_stdout.getvalue().strip()  # Получаем вывод в консоль
        self.assertEqual(output, "Покупатель авторизовался, можно продолжить покупки.")

if __name__ == '__main__':
    unittest.main()
