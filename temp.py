x = 3
y = 3
horseTuple = [
    (x - 2, y - 1),
    (x - 2, y + 1),
    (x - 1, y - 2),
    (x - 1, y + 2),
    (x + 1, y - 2),
    (x + 1, y + 2),
    (x + 2, y - 1),
    (x + 2, y + 1)
]

kingTuple = [
    (x + 1, y - 1),
    (x + 1, y),
    (x + 1, y + 1),
    (x, y - 1),
    (x, y + 1),
    (x - 1, y - 1),
    (x - 1, y),
    (x - 1, y + 1)
]

camelTuple = []

n = 6
x = 3
y = 3


def go_left_up(x, y):
    while x < n and 0 < y:
        camelTuple.append((x, y))
        x += 1
        y -= 1


def go_right_up(x, y):
    while x < n and y < n:
        camelTuple.append((x, y))
        x += 1
        y += 1


def go_left_down(x, y):
    while 0 < x and 0 < y:
        camelTuple.append((x, y))
        x -= 1
        y -= 1


def go_right_down(x, y):
    while 0 < x and y < n:
        camelTuple.append((x, y))
        x -= 1
        y += 1


go_left_up(x + 1, y - 1)
go_right_up(x + 1, y + 1)
go_left_down(x - 1, y - 1)
go_right_down(x - 1, y + 1)

print(camelTuple)
