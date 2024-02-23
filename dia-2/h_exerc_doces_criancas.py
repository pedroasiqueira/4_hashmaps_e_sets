a = [
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

def func(arr):
    c = set()
    for i, j in arr:
        c.add(i)
        c.add(j)
    return len(c)

print(func(a))