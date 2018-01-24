# Task:
# Write a function accepting a list of strings and a list of words
# and returns all the lines that contain the given words.
#
# Example:
# Lines: ['line with the keyword', 'incorrect line', 'searchword could be found here']
# Words: ['keyword', 'searchword']
# Result: ['line with the keyword', 'searchword could be found here']



class WordSearcher:
    def search(self, lines, words):
        answer = []
        for word in words:
            for line in lines:
                j = 0
                for symbol in line:
                    if symbol != word[j]:
                        j = 0
                    else:
                        j = j +1
                    if j == len(word):
                        answer.append(line)
                        break
        return answer
