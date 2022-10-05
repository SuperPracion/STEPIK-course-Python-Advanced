from math import sin, sqrt

def square(pair):
    return pair ** 2

def cube(pair):
    return pair ** 3

def sqrt_num(pair):
    return sqrt(pair)

def abs_num(pair):
    return abs(pair)

def sinus(pair):
    return sin(pair)

math_actions = {'квадрат': square, 'куб': cube, 'корень': sqrt_num, 'модуль': abs_num, 'синус': sinus}

num = int(input())
action = input()

print(math_actions[action](num))

