import random


def fisher_yates_randomize(arr, a, n):

    randoms = []
    k = 0
    for i in range(n):
        # Takes random integers n times O(n)
        j = random.randint(0, a-1)
        while j in randoms:
            j = random.randint(0, a-1)
        randoms.append(j)
    for i in range(a-1, -1, -1):
        if k >= n:
            # Break the shuffling process when randoms (list) comes to end
            # This reduces time complexity of this loop from O(a) to O(n)
            break
        j = randoms[k]
        k += 1
        arr[i], arr[j] = arr[j], arr[i]
    return arr
