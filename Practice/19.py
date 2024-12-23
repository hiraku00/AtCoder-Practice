import unittest
from fizzbuzz_for_19 import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    def test_fizzbuzz_with_1(self):
        self.assertEqual(fizzbuzz(1), ["1"])

    def test_fizzbuzz_with_3(self):
        self.assertEqual(fizzbuzz(3), ["1", "2", "Fizz"])

    def test_fizzbuzz_with_5(self):
        self.assertEqual(fizzbuzz(5), ["1", "2", "Fizz", "4", "Buzz"])

    def test_fizzbuzz_with_15(self):
        expected = ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
        self.assertEqual(fizzbuzz(15), expected)

    def test_fizzbuzz_with_0(self):
        self.assertEqual(fizzbuzz(0), [])
