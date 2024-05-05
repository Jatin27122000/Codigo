'''Write a Python program to find all anagrams of a string in a given list of strings using Lambda.
Orginal list of strings:
['bcda', 'abce', 'cbda', 'cbea', 'adcb']
Anagrams of 'abcd' in the above string:
['bcda', 'cbda', 'adcb']'''

original_list = ['bcda', 'abce', 'cbda', 'cbea', 'adcb']
target_string = 'abcd'
anagrams = list(filter(lambda x: sorted(x) == sorted(target_string), original_list))

print("Orginal list of strings:")
print(original_list)
print("Anagrams of '{}' in the above string:".format(target_string))
print(anagrams)
