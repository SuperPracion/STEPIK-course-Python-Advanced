with open('grades.txt', 'rt', encoding='utf-8') as file:
    count = 0
    for student_info in file.readlines():
        name, *grades = student_info.split()
        if sum(map(lambda x: int(x) >= 65, grades)) == 3:
            count += 1

    print(count)