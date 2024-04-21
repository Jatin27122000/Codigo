'''Write a  Python program to convert a given list of tuples to a list of lists.
Original list of tuples: [(1, 2), (2, 3), (3, 4)]
Convert the said list of tuples to a list of lists: [[1, 2], [2, 3], [3, 4]]
Original list of tuples: [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
Convert the said list of tuples to a list of lists: [[1, 2], [2, 3, 5], [3, 4], [2, 3, 4, 2]]'''

t1 = [(1, 2), (2, 3), (3, 4)]
t2 = [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]

r1 = [list(tup) for tup in t1]
r2 = [list(tup) for tup in t2]


print("Original list of tuples:")
print(t1)
print("Convert the said list of tuples to a list of lists:")
print(r1)

print("\nOriginal list of tuples:")
print(t2)
print("Convert the said list of tuples to a list of lists:")
print(r2)