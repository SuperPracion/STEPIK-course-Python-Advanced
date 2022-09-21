student_1, student_2, student_3 = [set(int(num) for num in input().split()) for _ in range(3)]

print((student_1 ^ student_2) | (student_3 ^ student_1))