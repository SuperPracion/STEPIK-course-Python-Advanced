n  = int(input())
k = int(input())
answer = 0

for i in range(1, n + 1):
    answer = (answer + k) % 1

print(answer + 1)