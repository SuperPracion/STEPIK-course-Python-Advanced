a, b, c = [int(input()) for _ in range(3)]
top_parabola = (-(b / (2 * a)),) + ((4 * a * c - (b * b)) / (4 * a),)

print(top_parabola)