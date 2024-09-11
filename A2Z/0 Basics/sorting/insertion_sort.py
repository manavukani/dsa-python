# take an element and place in correct order

# ------- Algorithm -------
# iteration 1: 1st element is already sorted
# iteration 2: if already sorted, break, else, place in correct order
# iteration 3: if already sorted, break, else, place in correct order
# .
# .
# .
# array is sorted


# ------- Complexity -------
# Time: O(n^2) - worst/avg case
# Space: O(1) - no extra space used

# ------- Implementation -------
def insertionSort(arr):
	n = len(arr) # Get the length of the array
	
	if n <= 1:
		return # If the array has 0 or 1 element, it is already sorted, so return

	for i in range(1, n): # Iterate over the array starting from the second element
		key = arr[i] # Store the current element as the key to be inserted in the right position
		j = i-1
		while j >= 0 and key < arr[j]: # Move elements greater than key one position ahead
			arr[j+1] = arr[j] # Shift elements to the right
			j -= 1
		arr[j+1] = key # Insert the key in the correct position

arr = [13, 46, 24, 52, 20, 9]
insertionSort(arr)
print(arr)
