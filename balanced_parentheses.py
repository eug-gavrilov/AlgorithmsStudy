# Task:
#
# Write a program to determine if the the parentheses (),
# the brackets [], and the braces {}, in a string are balanced.
#
# For example:
#
# {{)(}} is not balanced because ) comes before (
#
# ({)} is not balanced because ) is not balanced between {}
#      and similarly the { is not balanced between ()
#
# [({})] is balanced
#
# {}([]) is balanced
#
# {()}[[{}]] is balanced

class BalancedParentheses:
    def answer(self, line):
        print(line)
        count_a = 0
        count_b = 0
        count_c = 0
        last_symbol = ""
        for x in line:
            if x == "(":
                count_a +=1
                last_symbol = x
            if x == "{":
                count_b +=1
                last_symbol = x
            if x == "[":
                count_c += 1
                last_symbol = x
            if x == ")":
                count_a -=1
                if count_a < 0:
                    return False
                if last_symbol != "(":
                    return False
            if x == "}":
                count_b -= 1
                if count_b < 0:
                    return False
                if last_symbol != "{":
                    return False
            if x == "]":
                count_c -= 1
                if count_c < 0:
                    return False
                if last_symbol != "[":
                    return False
        if count_a == 0:
            return True
        if count_b == 0:
            return True
        if count_c == 0:
            return True
        return False