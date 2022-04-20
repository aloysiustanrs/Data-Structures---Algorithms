def selection_sort(arr):

    # Loop through all index except last one as the last index will be sorted
    # Set the minimum index as 'i'
    for i in range(len(arr) - 1):
        min_index = i

        # Find smallest in unsorted section
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap smallest in unsorted section with index at start of search
        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp
    return arr


arr = [9, 8, 6, 4, 3, 2, 1, 5]

print(selection_sort(arr))
