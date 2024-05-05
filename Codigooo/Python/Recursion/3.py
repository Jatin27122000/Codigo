'''Write a  Python program to sum recursion lists using recursion.
Test Data: [1, 2, [3,4], [5,6]]
Expected Result: 21'''

def sum_recursion(lst):
    total = 0
    for item in lst:
        if isinstance(item, list):
            total += sum_recursion(item)
        else:
            total += item
    return total

test_data = [1, 2, [3, 4], [5, 6]]
expected_result = 21
result = sum_recursion(test_data)

print("Result:", result)
print("Expected result:", expected_result)
print("Matched:", result == expected_result)
