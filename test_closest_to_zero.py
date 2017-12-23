import closest_to_zero
import unittest


class TestClosestToZero(unittest.TestCase):

    def test_returns_positive_if_equal(self):
        test_case = [-1, -5, 1, 6, 10]
        closest = closest_to_zero.ClosestToZero()
        answer = closest.answer(test_case)
        self.assertEqual(1, answer)

    def test_returns_zero_if_present(self):
        test_case = [-1, 0, 1]
        closest = closest_to_zero.ClosestToZero()
        answer = closest.answer(test_case)
        self.assertEqual(0, answer)

    def test_returns_closest_from_negative(self):
        test_case = [-5, -2, -1, -3]
        closest = closest_to_zero.ClosestToZero()
        answer = closest.answer(test_case)
        self.assertEqual(-1, answer)

    def test_returns_closest_of_positive(self):
        test_case = [3, 2, 3, 1]
        closest = closest_to_zero.ClosestToZero()
        answer = closest.answer(test_case)
        self.assertEqual(1, answer)

    def test_returns_number_from_given_array(self):
        test_case = [1, 2, 3]
        closest = closest_to_zero.ClosestToZero()
        answer = closest.answer(test_case)
        self.assertEqual(True, answer in test_case)


    unittest.main()
