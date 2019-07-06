# This problem was asked by Facebook.

# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

# You can assume that the messages are decodable. For example, '001' is not allowed.


# After playing with it on pen and paper I believe the best solution would be to look at the adjacent number to right.
# If the number is 1 the number to the right could be any number and that would be another correct permutation
# However, if it is 2 the number to the right must be a 6 or lower to be another correct permutation. 

def solution(number):
    if len(number) <= 1:
        return 1
    elif len(number) >= 2:
        if 1 <= int(''.join(number[0:2])) <= 26:
            return solution(number[1:]) + solution(number[2:])
        return solution(number[1:])

print(solution('12222'))