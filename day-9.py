# This problem was asked by Airbnb.

# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

# Follow-up: Can you do this in O(N) time and constant space?

# I went on the internet for this. The solution has to do with dynamic programming
testArray = [2, 4, 6, 2, 5]
def solution(array):
    if not array:
        return 0
    elif len(array) <= 2:
        return max(array)
    last_num = array[-1]  
    with_last = solution(array[:-2]) + last_num  
    without_last = solution(array[:-1])  
    return max(with_last, without_last)

print(solution(testArray))
