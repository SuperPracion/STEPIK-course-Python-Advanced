def func_apply(function, items):
    new_items = []
    for item in items:
        new_items.append(function(item))

    return new_items