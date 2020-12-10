import timeit
from search import Song_item, readfile


## Selection Sort (Source: https://www.geeksforgeeks.org/selection-sort/)
## Radix Sort (Source: https://www.geeksforgeeks.org/radix-sort/)

# Function to do sort
def selectionSort(arr):
    m = len(arr)
    # x = 0
    for i in range(m): #Upper loop
        min_val = min(arr[i:]) #Inner loop
    #För 100 element så blir det 100^2 gånger
        arr[i], arr[min_val.idx] = min_val, arr[i]
        """
        if ((100*i)//m) >x:
            print('#',end='')
            x+=1
        """

    return arr


##############################
# A function to do counting sort of arr[] according to
# the digit represented by exp.
def countingSort(arr, exp1):
    n = len(arr)

    # The output array elements that will have sorted arr
    output = [None] * (n)

    # initialize count array as 0
    count = [0] * (10)

    # Store count of occurrences in count[]
    for i in range(0, n):
        index = (arr[i].val // exp1)
        count[(index) % 10] += 1

    # Change count[i] so that count[i] now contains actual
    # position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]
        # Build the output array
    i = n - 1
    while i >= 0:
        index = (arr[i].val // exp1)
        output[count[(index) % 10] - 1] = arr[i]
        count[(index) % 10] -= 1
        i -= 1
    # Copying the output array to arr[],
    # so that arr now contains sorted numbers

    return output


# Method to do Radix Sort
def radixSort(arr):
    # Find the maximum number to know number of digits
    max1 = max(arr)
    print(max1.val)
    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1.val / exp > 0:
        arr = countingSort(arr, exp)
        exp *= 10

    return arr


def main():
    filename = "./unique_tracks.txt"
    lista = readfile(filename)

    # we can change the list here
    lista = lista[:1000]

    # n = len(lista)
    # search for the first occurance of artist name
    # Fast Sort

    radixtid = timeit.timeit(stmt=lambda: radixSort(lista), number=1)
    print("radixsort tog (Quick Sort) ", round(radixtid, 4), "sekunder")

    # slow sort
    selectiontid = timeit.timeit(stmt=lambda: selectionSort(lista), number=1)
    print("selectionsort tog (Slow Sort) ", round(selectiontid, 4), "sekunder")

    # Inte ett krav men tyckte att det skulle va bra för jämförelse
    linjtid = timeit.timeit(stmt=lambda: sorted(lista), number=1)
    print("Linjärsökningen tog (Python Sort) ", round(linjtid, 4), "sekunder")


if __name__ == "__main__":
    main()

#################################### Results ###################################
#            |   n=1 000     |   n=10 000    |   n=100 000    |   n=1000 000   |
# ____________|_______________|_______________|________________|________________|
# Fast Sorting|    0.2503     |     3.597     |    45.99       |     508        |
# ____________|_______________|_______________|________________|________________|
# Slow Sorting|     0.106     |     10.7202   |     1266       |    110000      |
# ____________|_______________|_______________|________________|________________|
# Python Sort |     0.0019    |     0.0328    |     0.4856     |    6.367       |
# ____________|_______________|_______________|________________|________________|


"""
Note : Number of repetitions in timing is only one for the large data cases (due to time issues)

Fast Sort is O(n)
Slow Sort is O(n*n)

"""
