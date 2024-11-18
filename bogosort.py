import random

def is_sorted(arr):
    """Check if the list is sorted"""
    return arr == sorted(arr)

def bogosort(arr):
    """Sorts an array using Bogosort"""
    while not is_sorted(arr):
        random.shuffle(arr)  # Shuffle the list randomly
    return arr

# Example usage
arr = [3, 2, 5, 1, 4]
print("Original list:", arr)
sorted_arr = bogosort(arr)
print("Sorted list:", sorted_arr)
