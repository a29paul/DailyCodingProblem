# This problem was asked by Twitter.

# Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

# For example, given the query string de and the set of strings[dog, deer, deal], return [deer, deal].

# Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.

# I will try to solve using brute force than optimize the code after
test =['dog', 'deer', 'deal']

def solution(query, array):
    sizeOfQueryString = len(query)
    filteredArray = []
    for string in array:
        substring = string[:sizeOfQueryString]
        if substring == query:
            filteredArray.append(string)
    return filteredArray

print(solution('de', test ))
# It seems that this is the most optimal solution as the time and space complexity is linear