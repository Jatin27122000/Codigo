'''Write a  Python program to find palindromes in a given list of strings using Lambda.
Orginal list of strings:
['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
List of palindromes:
['php', 'aaa']'''

original_list = ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
palindromes = list(filter(lambda x: x == x[::-1], original_list))
print("Orginal list of strings:")
print(original_list)
print("List of palindromes:")
print(palindromes)