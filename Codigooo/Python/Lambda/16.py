'''Write a Python program to find the second lowest total marks of any student(s) from the given names and marks of each student using lists and lambda. Input the number of students, the names and grades of each student.
Input number of students: 5
Name: S ROY
Grade: 1
Name: B BOSE
Grade: 3
Name: N KAR
Grade: 2
Name: C DUTTA
Grade: 1
Name: G GHOSH
Grade: 1
Names and Grades of all students:
[['S ROY', 1.0], ['B BOSE', 3.0], ['N KAR', 2.0], ['C DUTTA', 1.0], ['G GHOSH', 1.0]]
Second lowest grade: 2.0
Names:
N KAR'''

num_students = int(input("Input number of students: "))
student_list = []
for i in range(num_students):
    name = input("Name: ")
    grade = float(input("Grade: "))
    student_list.append([name, grade])

sorted_student_list = sorted(student_list, key=lambda x: x[1])
second_lowest_grade = sorted(set(grade for name, grade in sorted_student_list))[1]
names_with_second_lowest_grade = [name for name, grade in sorted_student_list if grade == second_lowest_grade]

print("Names and Grades of all students:")
print(sorted_student_list)
print("Second lowest grade:", second_lowest_grade)

print("Names:")
for name in names_with_second_lowest_grade:
    print(name)
