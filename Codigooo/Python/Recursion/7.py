'''Write a  Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0) using recursion .
Test Data:
sum_series(6) -> 12
sum_series(10) -> 30'''

def sum_series(n):
    if n <= 0:
        return 0
    else:
        return n + sum_series(n - 2)

test_cases = [6, 10]
for num in test_cases:
    print(f"sum_series({num}) -> {sum_series(num)}")
