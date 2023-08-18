def binary_search_recursive(arr, target, left, right):
    if left > right:
        return False
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return True
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

# Example list of numbers (sorted)
numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Get input from the user
target_number = int(input("Enter the number you want to search for: "))

# Call the recursive search function
found = binary_search_recursive(numbers, target_number, 0, len(numbers) - 1)

if found:
    print("Number found in the list.")
else:
    print("Number not found in the list.")