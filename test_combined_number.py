import unittest
import combined_number


class TestCombinedNumber(unittest.TestCase):
    def test_void_array_returns_void_string(self):
        test_case = []
        combined = combined_number.CombinedNumber()
        answer = combined.answer(test_case)
        self.assertEqual("", answer)

    def test_sorted_array_returns_the_same_order_string(self):
        test_case = [3, 2, 1]
        combined = combined_number.CombinedNumber()
        answer = combined.answer(test_case)
        self.assertEqual("321", answer)

    def test_not_sorted_numbers_smaller_than_ten_returns_ordered(self):
        test_case = [4, 2, 9, 8]
        combined = combined_number.CombinedNumber()
        answer = combined.answer(test_case)
        self.assertEqual("9842", answer)

    def test_not_sorted_numbers_with_bigger_than_ten_returns_ordered(self):
        test_case = [50, 2, 1, 9]
        combined = combined_number.CombinedNumber()
        answer = combined.answer(test_case)
        self.assertEqual("95021", answer)

    def test_when_opposit_order_returns_ordered(self):
        test_case = [50, 5, 56]
        combined = combined_number.CombinedNumber()
        answer = combined.answer(test_case)
        self.assertEqual("56550", answer)

    def test_when_big_numbers_returns_ordered(self):
        test_case = [420, 42, 423]
        combined = combined_number.CombinedNumber()
        answer = combined.answer(test_case)
        self.assertEqual("42423420", answer)


if __name__ == '__main__':
    unittest.main()
