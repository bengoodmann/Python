student_heights: list = input("Enter the heights of the students\n> ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_height: int = 0

for height in student_heights:
    total_height += height

print(f"Total height is {total_height}")

number_of_students: int = 0

for number in student_heights:
    number_of_students += 1

print(f"Total number of students is {number_of_students}")

average = round(total_height / number_of_students)
print(f"The average is {average}")