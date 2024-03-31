#Write a Python program to flatten a shallow list.
l=[["Gwalior","Bhopal"], ["Delhi","Indore"], ["Noida"]]
k= []

for x in l:
    for y in x:
        k.append(y)

print(k)
