synonyms_dict = {}

for _ in range(int(input())):
    key, synonyms = input().split()
    synonyms_dict[key], synonyms_dict[synonyms] = synonyms, key

search_synonym = input()
print(synonyms_dict[search_synonym])