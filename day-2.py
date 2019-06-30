# This problem was asked by Uber.

# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

# For example, if our input was[1, 2, 3, 4, 5], the expected output would be[120, 60, 40, 30, 24]. If our input was[3, 2, 1], the expected output would be[2, 3, 6].

# Follow-up: what if you can't use division?

array = [1, 2, 3, 4, 5]

# Obviously, the easiest way to do this would be do iterate through the array and then divide by the index you are on. 
# This is shown below:

def solution1(array):
    intermediateValue = 1
    i = 0
    for number in array:
        intermediateValue *= number
    while i<len(array):
        array[i] = intermediateValue/array[i]
        i = i + 1
    return array

# The solution below will take account the index and will not use divison in it's solution, however the the time complexity is
# O(n^2)
def solution2(array):
    resultArray = []
    for i in array:
        result = 1
        for j in array:
            if j!=i:
                result *= j
        resultArray.append(result)
    return resultArray

