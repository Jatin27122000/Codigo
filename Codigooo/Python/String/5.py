'''Write a  Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz
'''

s1 = 'abc'
s2 = 'xyz'
new_s1 = s2[:2] + s1[2:]
new_s2 = s1[:2] + s2[2:]
result = new_s1 + ' ' + new_s2
print(result)