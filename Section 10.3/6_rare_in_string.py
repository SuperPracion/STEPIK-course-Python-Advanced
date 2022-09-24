in_str = [word.strip('.,!?:;-') for word in input().lower().split()]

result = {}

for word in in_str:
    result[word] = result.get(word, 0) + 1

print(min([word for word in result.keys() if result[word] == min(result.values())]))