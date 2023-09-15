def quicksort(array):
    if len(array) < 2:
        return array  # Base case: arrays with 0 or 1 element are already “sorted.”
    else:
        pivot = array[0]  # Choose the pivot as the first element (for simplicity).
        less = [i for i in array[1:] if i <= pivot]  # Sub-array of all the elements less than or equal to the pivot.
        greater = [i for i in array[1:] if i > pivot]  # Sub-array of all the elements greater than the pivot.
        return quicksort(less) + [pivot] + quicksort(greater)  # Recursive case.

sorted_array = quicksort([10, 5, 2, 3])
print(sorted_array)
#this algorithm is O(n log n) in the average case, but O(n^2) in the worst case, the worst case is when the pivot is the smallest or largest element in the array, so we can avoid this by choosing a random element as the pivot.