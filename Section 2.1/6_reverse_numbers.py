in_num = input()

if len(in_num) >= 6:
    print(int(in_num[0] + in_num[-1:-6:-1]))
else:
    print(int(in_num[::-1]))
