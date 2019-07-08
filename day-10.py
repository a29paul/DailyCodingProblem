# This problem was asked by Apple.

# Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

# This question would be much easier to implement with JavaScript due to the built-in function timeout

# However, I will import a library to keep track of the time

import time

def solution(func, timeInSeconds):
    time.sleep(timeInSeconds)
    return func

def testFunc(x,y):
    return x+y

print(solution(testFunc(2,4),1))