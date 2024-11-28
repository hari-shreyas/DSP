def merge_sort(arr):
    if len(arr) <= 1:
        return arr           # If the list has 1 or fewer elements, it's already sorted, so return it
    
    mid = len(arr) // 2             # Find the middle point of the list to divide it into two halves
    left_half = arr[:mid]             # Split the list into two halves: left and right
    right_half = arr[mid:]
    
    left_half = merge_sort(left_half)       # Recursively sort both halves
    right_half = merge_sort(right_half)
    return merge(left_half, right_half)   # Merge the two sorted halves and return the result

def merge(left, right):
    """
    Function to merge two sorted lists into a single sorted list.
    It compares the elements of both lists and adds the smaller element to the merged list.
    """
    merged = []  # List to store the merged result
    left_index = 0  # Index for iterating over the left half
    right_index = 0  # Index for iterating over the right half
    
    while left_index < len(left) and right_index < len(right):  # Compare elements from both halves and add the smaller one to the merged list
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])  # Add smaller element from the left
            left_index += 1
        else:
            merged.append(right[right_index])  # Add smaller element from the right
            right_index += 1
   
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])    # If there are remaining elements in the left & right half, add them to the merged list
    return merged  # Return the fully merged and sorted list

if __name__ == '__main__':
    input_list = [1, 5, 6, 32, 15, -3]
    print('Original List:', input_list)
    sorted_list = merge_sort(input_list)
    print('Sorted List:', sorted_list)
