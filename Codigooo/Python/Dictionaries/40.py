
my_dict = {'x': list(range(11, 20)),
           'y': list(range(21, 30)),
           'z': list(range(31, 40))}

# Access the fifth value of each key
x_fifth_value = my_dict['x'][4]
y_fifth_value = my_dict['y'][4]
z_fifth_value = my_dict['z'][4]

# Print the fifth values
print(x_fifth_value)
print(y_fifth_value)
print(z_fifth_value)

# Print the dictionary
for key, value in my_dict.items():
    print(f"{key} has value {value}")
