student_1, student_2, student_3 = [set(int(num) for num in input().split()) for num in range(3)]

print(*(set(range(11)) - (student_1 | student_2 | student_3)))