import unittest
from scholarship import *

class TestAddFishToAquarium(unittest.TestCase):
    def test1(self):
        actual = check_scholarship_conditions(input1)
        expected = 'scholarship 50%'
        self.assertEqual(actual, expected)

    def test2(self):
        actual = check_scholarship_conditions(input2)
        expected = 'scholarship 100%'
        self.assertEqual(actual, expected)
    
    def test3(self):
        actual = check_scholarship_conditions(input3)
        expected = 'scholarship 0%'
        self.assertEqual(actual, expected)

input1 = {
    "average_grade": 3.2,
    "credit": 18,
    "trainning_point": 92
}
input2 = {
    "average_grade": 3.6,
    "credit": 18,
    "trainning_point": 92
}
input3 = {
    "average_grade": 3.1,
    "credit": 12,
    "trainning_point": 88
}