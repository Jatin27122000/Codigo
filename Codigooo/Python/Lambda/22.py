'''Write a  Python program that sums the length of a list of names after removing those that start with lowercase letters. Use the lambda function.
Result:
16'''

names_list = ['Alice', 'bob', 'Charlie', 'David', 'Emma', 'Frank']
result = sum(map(len, filter(lambda x: not x[0].islower(), names_list)))
print("Result:")
print(result)
