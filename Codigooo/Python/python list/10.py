#Write a Python program to find the list of words that are
# longer than n from a given list of words.

k= int(input("search longer no."))
print(k)
str ="The quick brown fox jumps over the lazy dog"
word=str.split(" ")
for str in word:
    if len(str)>k:
        print (str)