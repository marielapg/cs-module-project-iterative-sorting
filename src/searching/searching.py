def linear_search(arr, target):
    # Your code here
    for i in range(0, len(arr)):
	    if arr[i] == target:
	        return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    if len(arr) == 0:
        return -1
    left = 0
    right = len(arr) -1

    while left <= right:
        #find the midpoint 
        mid = (left + right) // 2
        #check to see if the midpoint element is our target 
        if arr[mid] == target:
            return mid
        #check to see if the element should be on the left or right side of our midpoint
        if arr[mid] < target:
            #toss out the left side of the arr
            #update our 'left' index
            left = mid +1 
        #otherwise, arr[mid] > target 
        else:
            # toss out the right side of the arr because the element has to be on the left side 
            right = mid -1
    return -1  # not found
