import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
from logic.employee import handle_employee
class TestHandleEmployee(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)  # Патчим sys.stdout для перехвата вывода в консоль
    @patch('tkinter.Tk')  # Мокаем Tkinter
    def test_handle_employee_success(self, MockTk, mock_stdout):
        # Мокаем создание окна Tkinter
        mock_window = MagicMock()
        MockTk.return_value = mock_window

        # Вызываем функцию
        handle_employee()

        # Проверяем, что продавец авторизовался
        output = mock_stdout.getvalue().strip()  # Получаем вывод в консоль
        self.assertEqual(output, "Продавец авторизовался, можно продолжить работу.")

if __name__ == '__main__':
    unittest.main()
