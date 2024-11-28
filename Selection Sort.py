def selection_sort(arr):
    n = len(arr)                                               # checks lengh of arrat
    for i in range(n):                                         #iterating through array
        min_index = i                                          #Assume the current index `i` holds the smallest element
        for j in range(i + 1, n):                              # Check the rest of the array (from i+1 to n) to find the smallest element
            if arr[j] < arr[min_index]:
                min_index = j                                  # Update min_index if a smaller element is found
        arr[i], arr[min_index] = arr[min_index], arr[i]        # Swap the smallest element found with the element at the current index `i`

if __name__ == "__main__":
    input_list = [64, 25, 12, 22, 11]
    print("Original List:", input_list)  
    selection_sort(input_list)
    print("Sorted List:", input_list)
