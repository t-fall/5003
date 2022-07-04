sequence = [5,11,17,23,25,30,39,44]#creates a sorted array to search
value = int(input("what number are you looking for?"))#gets user input for an integer search
length = len(sequence)#assigns the length of the array to a variable called length
middle = int(len(sequence)/2)#assignes the middle value of the array to middle
middlepos = sequence[middle]#assigns the middle position to a variable
while True:#creates a loop
    if len(sequence) > 1:#makes a check to see if the array still has elements inside to compare
        if middle == value:#if the middlemost value of the array is equal to the search value
            print("Found")#tells the user their value has been found in the array
            break#breaks the loop
        elif middle > value:#if the middle value in the array is greater than the search value...
            sequence = sequence[sequence > middlepos]#creates a new array using only the lower half of the array
        elif middle < value:#if the middle value in the array is less than the search value...
            sequence = sequence[sequence < middlepos]#creates a new array using only the greater half of the array
        else:
            print("not found")#tells the user that thair number could not be found
            break#breaks the loop
    else:
        print("not found")#tells the user that thair number could not be found
        break#breaks the loop