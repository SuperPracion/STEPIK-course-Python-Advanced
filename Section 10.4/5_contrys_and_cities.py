country_cities = {}

for _ in range(int(input())):
    country, *cities = input().split()
    for city in cities:
        country_cities[country] = city

for _ in range(int(input())):
    print(country_cities[input()])