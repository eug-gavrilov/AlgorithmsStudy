# Task:
# Given a list of integers find the closest to zero.
# If there is a tie, choose the positive value.


class ClosestToZero:
    def answer(self, numbers):

        closest = numbers[0]
        closest_len = abs(numbers[0])

        for i in range(len(numbers)):

            current = numbers[i]

            if abs(current) < closest_len or (abs(current) == closest_len and current > closest):
                closest = current
                closest_len = abs(current)

        return closest
