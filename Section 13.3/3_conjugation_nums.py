import cmath
n = int(input())
num1 = complex(input())
num2 = complex(input())

print(num1 ** n + num2 ** n + num1.conjugate() ** n + num2.conjugate() ** n + 1)
