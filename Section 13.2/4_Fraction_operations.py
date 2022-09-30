from fractions import Fraction
num1 = input()
num2 = input()

print(f'{num1} + {num2} = {Fraction(num1) + Fraction(num2)}')
print(f'{num1} - {num2} = {Fraction(num1) - Fraction(num2)}')
print(f'{num1} * {num2} = {Fraction(num1) * Fraction(num2)}')
print(f'{num1} / {num2} = {Fraction(num1) / Fraction(num2)}')