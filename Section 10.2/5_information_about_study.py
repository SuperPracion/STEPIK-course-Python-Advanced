info_about_study_dict = {'CS101': [3004, 'Хайнс', '8:00'], 'CS102': [4501, 'Альварадо', '9:00'],
                         'CS103': [6755, 'Рич', '10:00'], 'NT110': [1244, 'Берк', '11:00'],
                         'CM241': [1411, 'Ли', '13:00']}

course_key = input()
print('{0}: {1}, {2}, {3}'.format(course_key, *info_about_study_dict[course_key]))