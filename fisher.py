import random


def fisher_yates_randomize(arr, a, n):

    randoms = []
    k = 0
    for i in range(n):
        j = random.randint(0, a-1)
        while j in randoms:
            j = random.randint(0, a-1)
        randoms.append(j)
    for i in range(a-1, -1, -1):
        if k >= n:
            break
        j = randoms[k]
        k += 1
        arr[i], arr[j] = arr[j], arr[i]
    return arr
