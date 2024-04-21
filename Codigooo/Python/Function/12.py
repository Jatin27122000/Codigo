
'''Write a Python function that checks whether a passed string is a palindrome or not.
Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.'''
def fun(x):

    w = ""
    for i in x:
        w = i + w

    if (x == w):
        print("Yes")
    else:
        print("No")
        
x="madam"
print(fun(x))