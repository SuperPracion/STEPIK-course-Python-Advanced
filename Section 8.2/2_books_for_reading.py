n, m, k, x, y, z, t, a = [int(input()) for _ in range(8)]
x5 = t
x2 = m + n - x - t
x4 = n + k - z - t
x6 = m + k - y - t
x1 = n - x2 - x4 - x5
x3 = m - x2 - x5 - x6
x7 = k - x4 - x5 - x6

print(x7 + x1 + x3)
print(x4 + x2 + x6)
print(a - (x1 + x2 + x3 + x4 + x5 + x6 + x7))
