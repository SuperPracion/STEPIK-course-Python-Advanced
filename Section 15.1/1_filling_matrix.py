def matrix(n=1, m=0, value=0):
    return [[value] * (m if m else n) for _ in range(n)]

