# Given an array of integers, find the first missing positive integer in linear time and constant space. 

# In other words, find the lowest positive integer that does not exist in the array. 

# The array can contain duplicates and negative numbers as well.

# For example, the input[3, 4, -1, 1] should give 2. The input[1, 2, 0] should give 3.

array = [3, 4, -1, 1]

# Looking at the problem, I feel like the first thing I should do is sort it.
# The smallest number should be at the start of the array, and the largest number will be at the end
# I will do a merge sort first to sort the array, that takes O(nlogn)

def mergeSort(array):
    if len(array)>1:
        mid = len(array)/2
        leftHalf = array[:mid]
        rightHalf = array[mid:]

        i = 0
        j = 0
        k = 0
        while(i < len(leftHalf) and j < len(rightHalf)):
            if(leftHalf[i] <= rightHalf[j]):
                array[k] = leftHalf[i]
                i = i + 1
            else:
                array[k] = rightHalf[j]
                j = j + 1
            k = k + 1
        while(i<len(leftHalf)):
            array[k] = leftHalf[i]
            i = i + 1
            k = k + 1
        while(j<len(rightHalf)):
            array[k] = rightHalf[j]
            j = j + 1
            k = k + 1
        return array
# Now that I have merge sort defined what I will do next is find the first positive number in the index and take the last number in the array
def solution(array):
    sortedArray = mergeSort(array)
    lowestPositive = 0
    for number in sortedArray:
        if number > 0 :
            lowestPositive = number
            break
    indexStart = sortedArray.index(lowestPositive)
    nextLowest = lowestPositive
    i = indexStart
    while i < len(sortedArray):
        if nextLowest != sortedArray[i]:
            return nextLowest
        else:
            nextLowest = nextLowest + 1
            i = i + 1

# After solving, I realized that I don't need the greatest number. I just look through the array, incrementing a number that checks
# if it is incrementing by 1, if not, it return the next number.

# There is 2 loops and they are not nested, and we do not use more than one array, therefore the time and space complexity is linear
    


        
# Turns out that O(nlogn) is greater than O(n) therefore I am going to refactor my code to account for this
def filter(array):
    for i in array:
        if i < 0:
            array.pop(array.index(i))
    return array

# We will use the index of the number to keep track of whether we have seen the number or not
def indexTracker(array):
    i = 0
    while i < len(array):
        if array[i] < len(array):
            array[i] = array[i] * -1
            print(array)
        i = i+1
    return array

def solution2(array):
    positiveArray = filter(array)
    changedArray = indexTracker(positiveArray)
    for integer in changedArray:
        if integer >= 0:
            return changedArray.index(integer) + 1
print(solution2(array))
