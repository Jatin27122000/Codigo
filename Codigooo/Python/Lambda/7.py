'''Write a  Python program to find if a given string starts with a given character using Lambda.
Sample Output:
True
False'''

starts_with_char = lambda string, char: string.startswith(char)

string1 = "Python"
string2 = "C"

char1 = "o"
char2 = "C"

result1 = starts_with_char(string1, char1)
result2 = starts_with_char(string2, char2)

print(result1)  
print(result2) 
