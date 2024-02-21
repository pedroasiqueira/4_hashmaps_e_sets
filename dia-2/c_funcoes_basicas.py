list_a = [1, 3, 4, 3, 5, 1]
list_b = [2, 9, 4, 5, 9, 2]

# Transformar lista em conjunto:
set_a = set(list_a)
set_b = set(list_b)
print(set_a)
print(set_b)


# Operações em conjuntos:
# print(set_a.union(set_b))
# print(set_b.union(set_a, {10, 11, 12}))
# print(set_a.intersection(set_b))
# print(set_a.difference(set_b))
# print(set_b.difference(set_a))

# Operaçoes de comparação:
print(set_a == set_b)
print({1, 2, 3, 4} > {2, 3})
print({1, 2, 3} > {4, 5})