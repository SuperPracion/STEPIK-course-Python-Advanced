first_problem = set(int(num) for num in input().split())
second_problem = set(int(num) for num in input().split())

matching_elements = sorted(first_problem & second_problem, reverse=True)

if matching_elements:
    print(matching_elements)
else:
    print('BAD DAY')