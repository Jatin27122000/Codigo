'''Write a  Python program to check whether a given string is a number or not using Lambda.
Sample Output:
True
True
False
True
False
True
Print checking numbers:
True
True'''

is_number = lambda s: s.isdigit()
strings = ["123", "456.78", "abc", "-123", "1.0", "789"]
results = [is_number(s) for s in strings]
for s, result in zip(strings, results):
    print(f"{s}: {result}")
print("Print checking numbers:")
for s, result in zip(strings, results):
    if result:
        print(s)
