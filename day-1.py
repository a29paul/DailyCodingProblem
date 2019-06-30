# This problem was recently asked by Google.

# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given[10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?

arr = [10,15,3,7]
k = 17

# The easy way to do this with a high time complexity is to do nested for loops as shown below
def solution1(arr,k):
    for i in arr:
        for j in arr:
            if i+j==k:
                return True
# The one above is O(n^2) in terms of time complexity

# The solution below will use a merge sort to sort the array then solve it one pass. O(n log n) is the time complexity

def mergeSort(array):
    if len(array)>1:
        mid = len(array)/2
        leftHalf = array[:mid]
        rightHalf = array[mid:]
   
        mergeSort(leftHalf)
        mergeSort(rightHalf)

        i=0
        j=0
        k=0
        while i<len(leftHalf) and j<len(rightHalf):
            if leftHalf[i]<=rightHalf[j]:
                array[k] = leftHalf[i]
                i = i+1
            else:
                array[k] = rightHalf[j]
                j = j+1
            k = k+1
        while i < len(leftHalf):
            array[k] = leftHalf[i]
            i = i+1
            k = k+1
        while j < len(rightHalf):
            array[k] = rightHalf[j]
            j = j+1
        return array

def solution2(array, k):
    sortedArray = mergeSort(array)
    left = 0
    right = len(array)-1
    while left<right:
        if sortedArray[left] + sortedArray[right] == k:
            return True
        elif sortedArray[left] + sortedArray[right] < k:
            left = left + 1
        else: 
            right = right - 1
    return False
print(solution2(arr,k))
