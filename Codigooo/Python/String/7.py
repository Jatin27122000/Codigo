import re


str1 = 'The lyrics is not that poor!'
str2 = 'The lyrics is poor!'

# Define a regular expression pattern to match 'not' followed by 'poor'
pattern = re.compile(r'not.*?poor')

# Replace the matched pattern with 'good' if found, otherwise keep the original string
result1 = re.sub(pattern, 'good', str1)
result2 = re.sub(pattern, 'good', str2)

print("Result for '{}' : '{}'".format(str1, result1))
print("Result for '{}' : '{}'".format(str2, result2))
