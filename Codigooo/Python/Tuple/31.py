
tuple1 = (1, 2, 3, 4)
tuple2 = (3, 5, 2, 1)
tuple3 = (2, 2, 3, 1)

result = tuple(sum(x) for x in zip(tuple1, tuple2, tuple3))

print("Original lists:")
print(tuple1)
print(tuple2)
print(tuple3)
print("Element-wise sum of the said tuples:")
print(result)
