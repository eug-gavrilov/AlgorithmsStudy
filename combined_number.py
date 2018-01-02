# Task:
# Write a function accepting a list of non negative integers,
# and returning their largest possible combined number
# as a string. For example
#
# given [50, 2, 1, 9] it returns "95021"    (9 + 50 + 2 + 1)
# given [5, 50, 56]   it returns "56550"    (56 + 5 + 50)
# given [420, 42, 423] it returns "42423420" (42 + 423 + 420)

from random import random
def random_key(element):
    return random()
class CombinedNumber:
    def answer(self, numbers):
        a = sorted(numbers, reverse= True)
        a_1 = sorted(numbers, key=random_key)
        answer = ""
        answer_2 = ""
        for x in a:
           answer = answer + str(x)
        for y in a_1:
            answer_2 = answer_2 +str(y)
        if answer > answer_2:
            return answer
        return answer_2
