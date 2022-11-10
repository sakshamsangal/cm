x = set()
x.add((1, 2))
x.add((3, 4))

if (1, 2) in x:
    x.remove((1,2))
    print('yes')
    print(x)
else:
    print('no')
