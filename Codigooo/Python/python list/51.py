#Write a Python program to split a list every Nth element.
#n=3
l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
list1 = l[::3]
list2 = l[1::3]
list3 = l[2::3]

print([list1,list2,list3])