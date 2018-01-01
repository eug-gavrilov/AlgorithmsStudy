import balanced_parentheses
import unittest


class TestBalancedParentheses(unittest.TestCase):

    def test_returns_false_when_unbalanced_mixed_group_three_types(self):
        line = "[{{)(}}]"
        algorithm = balanced_parentheses.BalancedParentheses()
        result = algorithm.answer(line)
        self.assertEqual(False, result)

    def test_returns_false_when_unbalanced_mixed_group_two_types(self):
        line = "({)}"
        algorithm = balanced_parentheses.BalancedParentheses()
        result = algorithm.answer(line)
        self.assertEqual(False, result)

    def test_returns_true_when_balanced_mixed_group(self):
        line = "{()}[[{}]]"
        algorithm = balanced_parentheses.BalancedParentheses()
        result = algorithm.answer(line)
        self.assertEqual(True, result)

    def test_returns_true_on_balance_of_separate_pairs_of_braces(self):
        line = "{}{}"
        algorithm = balanced_parentheses.BalancedParentheses()
        result = algorithm.answer(line)
        self.assertEqual(True, result)

    def test_returns_true_on_balance_of_inclusive_braces(self):
        line = "{{}}"
        algorithm = balanced_parentheses.BalancedParentheses()
        result = algorithm.answer(line)
        self.assertEqual(True, result)

    def test_returns_true_on_balance_of_two_braces(self):
        line = "{}"
        algorithm = balanced_parentheses.BalancedParentheses()
        result = algorithm.answer(line)
        self.assertEqual(True, result)

    def test_returns_true_on_balance_of_separate_pairs_of_brackets(self):
        line = "[][]"
        algorithm = balanced_parentheses.BalancedParentheses()
        result = algorithm.answer(line)
        self.assertEqual(True, result)

    def test_returns_true_on_balance_of_inclusive_brackets(self):
        line = "[[]]"
        algorithm = balanced_parentheses.BalancedParentheses()
        result = algorithm.answer(line)
        self.assertEqual(True, result)

    def test_returns_true_on_balance_of_two_brackets(self):
        line = "[]"
        algorithm = balanced_parentheses.BalancedParentheses()
        result = algorithm.answer(line)
        self.assertEqual(True, result)

    def test_returns_true_on_balance_of_separate_pairs_of_parentheses(self):
        line = "()()"
        algorithm = balanced_parentheses.BalancedParentheses()
        result = algorithm.answer(line)
        self.assertEqual(True, result)

    def test_returns_true_on_balance_of_inclusive_parentheses(self):
        line = "(())"
        algorithm = balanced_parentheses.BalancedParentheses()
        result = algorithm.answer(line)
        self.assertEqual(True, result)

    def test_returns_false_when_parentheses_not_opened(self):
        line = ")()"
        algorithm = balanced_parentheses.BalancedParentheses()
        result = algorithm.answer(line)
        self.assertEqual(False, result)

    def test_returns_false_when_parentheses_not_closed(self):
        line = "(()"
        algorithm = balanced_parentheses.BalancedParentheses()
        result = algorithm.answer(line)
        self.assertEqual(False, result)

    def test_returns_true_on_balance_of_two_parentheses(self):
        line = "()"
        algorithm = balanced_parentheses.BalancedParentheses()
        result = algorithm.answer(line)
        self.assertEqual(True, result)

    def test_returns_true_on_void_string(self):
        line = ""
        algorithm = balanced_parentheses.BalancedParentheses()
        result = algorithm.answer(line)
        self.assertEqual(True, result)


if __name__ == '__main__':
    unittest.main()
