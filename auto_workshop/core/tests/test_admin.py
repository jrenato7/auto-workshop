from django.test import TestCase

from auto_workshop.core.admin import format_currency


class TestCurrencyFormat(TestCase):
    def test_format_currency(self):
        value = 20.00
        resp = format_currency(value)
        self.assertEqual("R$ 20.00", resp)
