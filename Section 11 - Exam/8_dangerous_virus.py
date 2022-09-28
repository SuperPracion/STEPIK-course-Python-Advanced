actions = {'read': 'R', 'write': 'W', 'execute': 'X'}

files = {}
for _ in range(int(input())):
    file_name, *action = input().split()
    files[file_name] = action

for _ in range(int(input())):
    action, file_name = input().split()
    if actions[action] in files[file_name]:
        print('OK')
    else:
        print('Access denied')
