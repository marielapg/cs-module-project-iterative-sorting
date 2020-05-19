# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
    for j in range(cur_index, len(arr)):
        if arr[j] < arr[smallest_index]:
            smallest_index = j

        # TO-DO: swap
        # Your code here
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    swaps_occurred = True
    while swaps_occurred:
        swaps_occurred = False
        for i in range(0,len(arr)-1):
            if(arr[i] > arr[i + 1]):
                #swap
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swaps_occured = True
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here
    if len(arr) == 0:   
        return arr
    # if maximum is not given, we'll take the max value from input array 
    if maximum == -1:
        maximum = max(arr)
    # make a bunch of buckets 
    buckets = [0 for i in range(maximum+1)]

    for x in arr:
        if x < 0:
            return "Error, negative numbers not allowed"
        buckets[x] += 1

    # we have the counts of every value in our input array
    # loop through our buckets, starting at the smallest index
    j = 0
    for i in range(len(buckets)):
        while buckets[i] > 0:
            arr[j] = i
            j += 1
            buckets[i] -= 1

    return arr
