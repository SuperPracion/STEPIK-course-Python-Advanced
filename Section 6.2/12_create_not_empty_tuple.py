tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
non_empty_tuples = [tuple(element) for element in tuples if len(element)]

print(non_empty_tuples)