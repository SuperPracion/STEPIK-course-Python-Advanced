in_str = input().lower()
do_not_use_symbols = ['.', ',', ';', ':', '-', '?', '!',]

# for symbol in in_str:
#     if symbol in do_not_use_symbols:
#         in_str = in_str.replace(symbol, '')

for symbol in do_not_use_symbols:
    in_str = in_str.replace(symbol, '')

print(len(set(in_str.split())))