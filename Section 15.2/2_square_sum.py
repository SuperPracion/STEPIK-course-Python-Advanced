def sq_sum(*args):
    return sum([float(i) ** 2 for i in args])


print(sq_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))