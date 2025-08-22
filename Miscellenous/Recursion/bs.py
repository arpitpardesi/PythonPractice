a = [6,2,7,2,7,3,4,5,6,7,8,9,10,11,12,13,14,15]

def binary_search(arr, target, low, high):
    if low > high:
        return -1  # Target not found

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid  # Target found
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)  # Search in the right half
    else:
        return binary_search(arr, target, low, mid - 1)  # Search in the left half

def search(arr, target):
    arr.sort()  # Ensure the array is sorted
    return binary_search(arr, target, 0, len(arr) - 1)

# Example usage
target = 7
result = search(a, target)
if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the array.")
