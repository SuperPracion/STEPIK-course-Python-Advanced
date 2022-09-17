n = int(input())
students = [tuple(input().split()) for _ in range(n)]

for student in students:
    print(*student)

print()

for student in students:
    if student[1] in ('4', '5'):
        print(*student)