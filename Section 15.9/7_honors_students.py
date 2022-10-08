students = []
for _ in range(int(input())):
    temp = {}
    for _ in range(int(input())):
        student = input().split()
        temp[student[0]] = student[1]

    students.append(temp)

print('YES' if all(any('5' == i for i in list(i.values())) for i in students) else 'NO')
# print(all([any() for stud_glop in students]))