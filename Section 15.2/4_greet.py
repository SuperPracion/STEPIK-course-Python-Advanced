def greet(name, *args):
    return f"Hello, {' and '.join([name, *list(args)])}!"

print(greet('Soltan', 'Marko'))