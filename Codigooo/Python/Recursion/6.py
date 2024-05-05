''' Write a Python program to get the sum of a non-negative integer using recursion.
Test Data:
sumDigits(345) -> 12
sumDigits(45) -> 9'''

def sum_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_digits(n // 10)

test_cases = [345, 45]
for num in test_cases:
    print(f"sumDigits({num}) -> {sum_digits(num)}")
