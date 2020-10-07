



# Algorithm:
# 1. Scan the array from left to right, exchange pairs of elements that are out-oforder.
# 2. Repeat the above process for (N-1) time where N is the number of elements
# in the array.


# This function will loop through the array for n time (n: length of array)
def bubble_sort(a : list ):

    n = len(a)
    for i in range(0, n):
        #print(a)
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
    return a

def bubble_sort_optimize(a: list):
    is_sorted = False
    n = len(a)

    while is_sorted == False:

        is_sorted = True
        for i in range(0, n-1):
            #print(a)
            if a[i] > a[i+1]:
                temp = a[i]
                a[i] = a[i+1]
                a[i+1] = temp
                is_sorted = False

    return a






a = [ 25 ,57 ,48 ,37, 12, 92 ,86, 33]
print('original: ', a)
print('(1) sorted: ', bubble_sort(a))



print('(2) sorted: ', bubble_sort_optimize(a))
