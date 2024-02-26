friends = [
    ('Dani', 'Ali'),
    ('Fabi', 'Zizu'),
    ('Gabi', 'Ito'),
    ('Fabi', 'Rafa'),
    ('Ali', 'Fabi'),
    ('Rafa', 'Lulu'),
    ('Gabi', 'Hos'),
    ('Eli', 'Hos'),
    ('Hos', 'Dani'),
    ('Zizu', 'Gabi'),
    ('Fabi', 'Gabi'),
    ]

# Porque não pega todos os nomes?
# c = {value for value, value in friends}
# print(c)

# MINHA RESOLUÇÃO:
def func(arr):
    c = set()
    for i, j in arr:
        c.add(i)
        c.add(j)
    d = {value: set() for value in c}

    for i, j in arr:
        if i in d:
            d[i].add(j)
        if j in d:
            d[j].add(i)
    return d

# RESOLUÇÃO COURSE:
def func22(arr):
    c = {}
    for i, j in arr:
        if i not in c:
            c[i] = set()
        if j not in c:
            c[j] = set()
        c[i].add(j)
        c[j].add(i)

    return c
        

func1 = func(friends)
# print(func1)

func2 = func22(friends)
print(func2)

# for i, j in dd.items():
#     print(i, j)

# for i, j in friends:
#     print(i, j)