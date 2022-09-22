m, n = [int(input()) for _ in range(2)]
books_at_home = [input() for _ in range(m)]
need_read_books = [input() for _ in range(n)]

for need_read in need_read_books:
    if need_read in books_at_home:
        print('YES')
    else:
        print('NO')