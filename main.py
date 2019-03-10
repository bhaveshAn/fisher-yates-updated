# This is the driver program

from fisher import fisher_yates_randomize

a = int(input('Enter the number of elements in the array : '))
arr = [int(x) for x in input().strip().split()]
n = int(input('Enter the number of elements to shuffle : '))
print(fisher_yates_randomize(arr, a, n))
