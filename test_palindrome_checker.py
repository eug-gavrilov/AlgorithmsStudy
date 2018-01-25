import unittest
import palindrome_checker


class TestPalindromeCheckers(unittest.TestCase):
    def test_mixed_not_palindrome_returns_false(self):
        test_case = "Not a palindrome!"
        checker = palindrome_checker.PalindromeChecker()
        answer = checker.check(test_case)
        self.assertFalse(answer)

    def test_simple_not_palindrome_returns_false(self):
        test_case = "london"
        checker = palindrome_checker.PalindromeChecker()
        answer = checker.check(test_case)
        self.assertFalse(answer)

    def test_mixed_chars_and_punctuation_palindrome_returns_true(self):
        test_case = "Mr. Owl ate my metal worm"
        checker = palindrome_checker.PalindromeChecker()
        answer = checker.check(test_case)
        self.assertTrue(answer)

    def test_lowercase_simple_string_palindrome_returns_true(self):
        test_case = "madam"
        checker = palindrome_checker.PalindromeChecker()
        answer = checker.check(test_case)
        self.assertTrue(answer)

    def test_single_char_string_is_palindrome(self):
        test_case = "a"
        checker = palindrome_checker.PalindromeChecker()
        answer = checker.check(test_case)
        self.assertTrue(answer)

    def test_void_string_is_palindrome(self):
        test_case = ""
        checker = palindrome_checker.PalindromeChecker()
        answer = checker.check(test_case)
        self.assertTrue(answer)


if __name__ == '__main__':
    unittest.main()
