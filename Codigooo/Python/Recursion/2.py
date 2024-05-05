'''Write a Python program to convert an integer to a string in any base using recursion .'''

def convert_to_base(n, base):
    if n == 0:
        return ""
    else:
        remainder = n % base
        return convert_to_base(n // base, base) + str(remainder)

number = 123
base = 2
print(f"{number} in base {base}: {convert_to_base(number, base)}")
