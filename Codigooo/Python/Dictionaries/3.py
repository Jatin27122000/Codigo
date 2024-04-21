"""
3. Write a Python script to concatenate following dictionaries to create
a new one. 
Sample Dictionary : 
dic1={1:10, 2:20} 
dic2={3:30, 4:40} 
dic3={5:50, 6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
"""

dict1={1:10, 2:20} 
dict2={3:30, 4:40} 
dict3={5:50, 6:60}

combined_dict = {k: v for k, v in dict1.items() | dict2.items() | dict3.items()}
print(combined_dict)
