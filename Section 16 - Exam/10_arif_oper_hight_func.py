import operator

def arithmetic_operation(operation):
    operations = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    return operations[operation]

add = arithmetic_operation('+')
div = arithmetic_operation('/')
print(add(10, 20))
print(div(20, 5))