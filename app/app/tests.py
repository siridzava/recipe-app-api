from django.test import TestCase
from .calc import add, subtract


class CalcTests(TestCase):

    def test_add_numbers(self):
        self.assertEqual(add(3, 19), 22)

    def test_subtract_numbers(self):
        self.assertEqual(subtract(95, 37), 58)
