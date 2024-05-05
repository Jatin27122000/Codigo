'''Write a  Python program to filter the height and width of students, which are stored in a dictionary using lambda.
Original Dictionary:
{'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
Height> 6ft and Weight> 70kg:
{'Cierra Vega': (6.2, 70)}'''

students = {
    'Cierra Vega': (6.2, 70),
    'Alden Cantrell': (5.9, 65),
    'Kierra Gentry': (6.0, 68),
    'Pierre Cox': (5.8, 66)
}

filtered_students = dict(filter(lambda item: item[1][0] > 6 and item[1][1] > 70, students.items()))

print("Original Dictionary:")
print(students)
print("Height > 6ft and Weight > 70kg:")
print(filtered_students)
