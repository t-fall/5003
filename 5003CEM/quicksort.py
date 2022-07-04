def quicksort(left, right, array): #creates the fucntion to sort the data
    if left < right:
        partitionpointer = partition(left, right, array)
        quicksort(left, partitionpointer - 1, array)
        quicksort(partitionpointer + 1, right, array)

def partition(left, right, array):#creates the function to search through the array
    middle = int(len(array)/2)#assigns an integer value to the middle element of the array
    print(array[middle])
    pivot = array[middle]#assigns the pivot position to the middle of the array
    while left > right:#creates a loop for as long as left is greater than right
        while left < right and array[left] < pivot:#creates a second loop as long as left is less than right and the left is less than the pivot
            left = left + 1#incrementally increases the left value by one
        while right > left and array[right] >= pivot:
            right = right - 1#incrementally decreases the right value by one
        if left < right:
            array[left], array[right] = array[right], array[left]#swaps the psotions of the left varialbe and the right variable
    if array[left] > pivot:
        array[left], array[right] = array[right], array[left]#swaps the psotions of the left varialbe and the right variable

    return left

ararray = [3,4,6,2,8,7,1,5,9]
quicksort(0, len(array)-1, array)
print(array)