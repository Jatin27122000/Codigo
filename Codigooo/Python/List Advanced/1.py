'''Write a Python function to reverse a list at a specific location.'''

def reverse_list_at_location(l, location):
    if location < 0 or location >= len(l):
        print("Invalid location")
        return l
    else:
        left = l[:location]
        right = l[location:]
        reversed_right_part = right[::-1]
        return left + reversed_right_part

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
location = 3
print(reverse_list_at_location(my_list, location))  
