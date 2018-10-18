import unittest
from intArrayToPhoneNumber import *
from sortGivenString import *


class TestStringMethods(unittest.TestCase):

    def test_phoneNumberConverter(self):
        self.assertEqual(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
        self.assertEqual(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), "(111) 111-1111")
        self.assertEqual(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
        self.assertEqual(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]), "(023) 056-0890")
        self.assertEqual(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), "(000) 000-0000")

    def test_sortGivenString(self):
        self.assertEqual(order("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est")


if __name__ == '__main__':
    unittest.main()