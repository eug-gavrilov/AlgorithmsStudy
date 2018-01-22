import unittest
import word_searcher


class TestWordSearcher(unittest.TestCase):
    def test_finds_attached_words(self):
        test_case = ['incorrectline', 'line with thekeyword']
        searcher = word_searcher.WordSearcher()
        answer = searcher.search(test_case, ['keyword'])
        self.assertEqual(test_case[0], answer[0])

    def test_returns_array_of_correct_lines_with_all_keywords(self):
        test_case = ['line with the keyword', 'incorrect line', 'searchword could be found here']
        searcher = word_searcher.WordSearcher()
        answer = searcher.search(test_case, ['keyword', 'searchword'])
        self.assertEqual(2, len(answer))
        self.assertEqual(test_case[0], answer[0])
        self.assertEqual(test_case[2], answer[1])

    def test_returns_array_of_correct_lines(self):
        test_case = ['line with the keyword', 'incorrect line', 'another keyword line']
        searcher = word_searcher.WordSearcher()
        answer = searcher.search(test_case, ['keyword'])
        self.assertEqual(2, len(answer))
        self.assertEqual(test_case[0], answer[0])
        self.assertEqual(test_case[2], answer[1])

    def test_returns_only_correct_line(self):
        test_case = ['line with the keyword', 'incorrect line']
        searcher = word_searcher.WordSearcher()
        answer = searcher.search(test_case, ['keyword'])
        self.assertEqual(1, len(answer))

    def test_returns_line_if_has_keyword(self):
        test_case = ['line with the keyword']
        searcher = word_searcher.WordSearcher()
        answer = searcher.search(test_case, ['keyword'])
        self.assertEqual(test_case[0], answer[0])

    def test_returns_nothing_if_nothing_matchs(self):
        test_case = ['asd', 'asdasd dsasdas', 'ewfdsfsdf']
        searcher = word_searcher.WordSearcher()
        answer = searcher.search(test_case, ['test', 'nothing'])
        self.assertEqual(0, len(answer))

    def test_returns_nothing_if_nothing_sent(self):
        test_case = []
        searcher = word_searcher.WordSearcher()
        answer = searcher.search(test_case, [])
        self.assertEqual(0, len(answer))


if __name__ == '__main__':
    unittest.main()
