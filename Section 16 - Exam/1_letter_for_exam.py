def generate_letter(mail, name, date, time, place, teacher='Тимур Гуев', number=17):
    mail = f'To: {mail}\n' \
           f'Приветствую, {name}!\n' \
           f'Вам назначен экзамен, который пройдет {date}, в {time}.\n' \
           f'По адресу: {place}.\n' \
           f'Экзамен будет проводить {teacher} в кабинете {number}.\n' \
           f'Желаем удачи на экзамене!'

    return mail

print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00', 'Часова 23, корпус 2'))
print()
print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00', 'Часова 23, корпус 2', 'Василь Ярошевич', 23))