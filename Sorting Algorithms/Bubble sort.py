
def bubble_sort(array):
    n = len(array)

    # Increment i for every one loop
    for i in range(n):

        # For range of n-i-1, the range gets smaller everytime as the unsorted portion gets smaller
        # Sorted portion on the right increases for each 'for j' iteration
        for j in range(n - i - 1):

            # Compare two adjacent index , if left > right , swap
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]



    return array


arr = [9, 8, 6, 4, 3, 2, 1, 5]
print(bubble_sort(arr))
