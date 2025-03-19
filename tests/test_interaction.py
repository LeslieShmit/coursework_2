import unittest
from unittest.mock import patch

from src.interaction import interact


class TestInteract(unittest.TestCase):

    @patch("builtins.input", return_value="5")
    def test_interact_incorrect_selection(self, mock_input):
        with patch("builtins.print") as mock_print:
            interact()
            mock_print.assert_called_with(
                "Введенные вами данные некорректны. Завершение работы программы."
            )
