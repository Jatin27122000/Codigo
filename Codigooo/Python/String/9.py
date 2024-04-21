str1 = "jatin kanoje"
n=4
str1=list(str1)
print("Modified string after removing ", n, "th character ")
del str1[n]
#printing as list
print(''.join(str1))