from random import *

secret_friends = dict()
applicants = [input() for _ in range(int(input()))]

for human in applicants:
    secret_friends.setdefault(human, '')

for human in secret_friends.keys():
    shuffle(applicants)
    for i in range(len(applicants)):
        if applicants[i] != human and applicants[i] not in secret_friends.values():
            secret_friends[human] = applicants[i]
            del applicants[i]
            break

for student, friend in secret_friends.items():
    print(f'{student} - {friend}')


