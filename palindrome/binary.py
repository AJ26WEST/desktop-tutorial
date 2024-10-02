# Define the sorted array and the target value
array = [3, 4, 5, 6, 7, 8, 9]
target = 4

# Initialize the low and high pointers
low = 0
high = len(array) - 1

# Repeat until the pointers low and high meet
found = False  # Variable to track if the target is found
index = -1  # Variable to store the index of the target

while low <= high:
    # Find the middle index
    mid = (low + high) // 2
    
    # Check if the target is at the mid index
    if array[mid] == target:
        found = True
        index = mid  # Target found, store its index
        break  # Exit the loop since we found the target
    elif array[mid] < target:
        # If the target is greater, ignore the left half
        low = mid + 1
    else:
        # If the target is smaller, ignore the right half
        high = mid - 1

# Print the result
if found:
    print("Element is present at index " + str(index))
else:
    print("Not found")
