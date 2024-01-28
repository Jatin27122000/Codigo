#Write a Python program to convert temperatures to and from Celsius and Fahrenheit.
#[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
#Expected Output :
#60°C is 140 in Fahrenheit
#45°F is 7 in Celsius

x= float(input("enter Cel: "))
print(x)
y= float(input("enter far: "))
print(y)

far = (x * 1.8) + 32
print("temp in celsius to fahrenheit", far)

celc = (y - 32) * 5/9
print("temp in fahrenheit to celsius ", celc)