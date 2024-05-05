'''Write a Python program to create Fibonacci series up to n using Lambda.
Fibonacci series upto 2:
[0, 1]
Fibonacci series upto 5:
[0, 1, 1, 2, 3]
Fibonacci series upto 6:
[0, 1, 1, 2, 3, 5]
Fibonacci series upto 9:
[0, 1, 1, 2, 3, 5, 8, 13, 21]'''

fibonacci_series = lambda n: [0, 1] if n <= 2 else fibonacci_series(n-1) + [fibonacci_series(n-1)[-1] + fibonacci_series(n-2)[-1]]
for n in [2, 5, 6, 9]:
    print(f"Fibonacci series up to {n}:")
    print(fibonacci_series(n))
