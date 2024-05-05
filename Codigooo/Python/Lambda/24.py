'''Write a  Python program to find numbers within a given range where every number is divisible by every digit it contains.
Sample Output:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]'''

start = 1
end = 100
def check_divisibility(num):
    return all(num % int(digit) == 0 for digit in str(num) if digit != '0')

result = list(filter(check_divisibility, range(start, end + 1)))

print("Sample Output:")
print(result)