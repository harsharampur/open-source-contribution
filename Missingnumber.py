def missing_number(n, arr):
    # Create hash array of size n+1
    hash = [0] * (n + 1)

    # Store frequencies of elements
    for num in arr:
        hash[num] += 1

    # Find the missing number
    for i in range(1, n + 1):
        if hash[i] == 0:
            return i

    # Edge case handling (though problem guarantees a solution)
    return -1


# Driver code
arr = [1, 2, 3, 5]
n = 5
print(missing_number(n, arr))
