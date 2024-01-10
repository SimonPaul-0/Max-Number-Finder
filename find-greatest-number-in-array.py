def find_greatest_number(arr):
    if not arr:
        return "Array is empty"

    greatest = arr[0]
    for num in arr:
        if num > greatest:
            greatest = num

    return greatest

# Input: Enter numbers separated by space (e.g., 12 5 27 8 15 20)
user_input = input("Enter numbers separated by space: ")
numbers = [int(x) for x in user_input.split()]

result = find_greatest_number(numbers)

print(f"The greatest number in the array is: {result}")
