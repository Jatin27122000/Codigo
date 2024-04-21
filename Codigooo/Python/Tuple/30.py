tuple = (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime')) 
ele="pink"
x=[ele for i in tuple if ele in i] 
print(["yes" if x else "no"])
