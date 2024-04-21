#



str = "jatinkanoje"
count = 0
for i in str:
	count = count + 1
nstr = str[ 0:2 ] + str [count - 2: count ] 

print("Input string = " + str)
print("New String = "+ nstr)
