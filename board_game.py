def process_horse(x, y, n, arr):
    horse_square = set()
    horse_square.add((x - 2, y - 1))
    horse_square.add((x - 2, y + 1))
    horse_square.add((x - 1, y - 2))

    horse_square.add((x - 1, y + 2))
    horse_square.add((x + 1, y - 2))
    horse_square.add((x + 1, y + 2))

    horse_square.add((x + 2, y - 1))
    horse_square.add((x + 2, y + 1))

    poss_square = 8
    for a, b in horse_square:
        if a < 1 or n < a or b < 1 or n < b:
            poss_square -= 1
    for item in arr:
        if item in horse_square:
            poss_square -= 1
    return poss_square


def process_king(x, y, n, arr):
    king_square = set()
    king_square.add((x + 1, y - 1))
    king_square.add((x + 1, y))
    king_square.add((x + 1, y + 1))
    king_square.add((x, y - 1))
    king_square.add((x, y + 1))
    king_square.add((x - 1, y - 1))
    king_square.add((x - 1, y))
    king_square.add((x - 1, y + 1))
    #  check for valid squares
    poss_square = 8
    for a, b in king_square:
        if a < 1 or n < a or b < 1 or n < b:
            poss_square -= 1
    for item in arr:
        if item in king_square:
            poss_square -= 1
    return poss_square


camel_square = {
    "up_left": set(),
    "up_right": set(),
    "down_left": set(),
    "down_right": set()
}

d = {
    "up_left": set(),
    "up_right": set(),
    "down_left": set(),
    "down_right": set()
}


def go_left_up(x, y, n):
    while x < n and 0 < y:
        camel_square['up_left'].add((x, y))
        x += 1
        y -= 1
    min_a = 100001
    min_tup = -1
    for item in d['up_left']:
        if item in camel_square['up_left']:
            a, b = item
            if a < min_a:
                min_a = a
                min_tup = (a, b)

    my_len = len(camel_square['up_left'])
    if min_a != 100001:
        x, y = min_tup
        while x < n and 0 < y:
            x += 1
            y -= 1
            my_len -= 1
    return my_len


def go_right_up(x, y, n):
    while x < n and y < n:
        camel_square['up_right'].add((x, y))
        x += 1
        y += 1

    min_a = 100001
    min_tup = -1
    for item in d['up_right']:
        if item in camel_square['up_right']:
            a, b = item
            if a < min_a:
                min_a = a
                min_tup = (a, b)

    my_len = len(camel_square['up_right'])
    if min_a != 100001:
        x, y = min_tup
        while x < n and y < n:
            x += 1
            y += 1
            my_len -= 1
    return my_len


def go_left_down(x, y):
    while 0 < x and 0 < y:
        camel_square['down_left'].add((x, y))
        x -= 1
        y -= 1

    max_a = -1
    max_tup = -1
    for item in d['down_left']:
        if item in camel_square['down_left']:
            a, b = item
            if max_a < a:
                max_a = a
                max_tup = (a, b)

    my_len = len(camel_square['down_left'])
    if max_a != -1:
        x, y = max_tup
        while 0 < x and 0 < y:
            x -= 1
            y -= 1
            my_len -= 1
    return my_len


def go_right_down(x, y, n):
    while 0 < x and y < n:
        camel_square['down_right'].add((x, y))
        x -= 1
        y += 1
    max_a = -1
    max_tup = -1
    for item in d['down_right']:
        if item in camel_square['down_right']:
            a, b = item
            if max_a < a:
                max_a = a
                max_tup = (a, b)

    my_len = len(camel_square['down_right'])
    if max_a != -1:
        x, y = max_tup
        while 0 < x and y < n:
            x -= 1
            y += 1
            my_len -= 1
    return my_len


def cat_quadrant(x, y, item):
    a, b = item
    if x < a:
        if b < y:
            d['up_left'].add(item)
        elif y < b:
            d['up_right'].add(item)
    else:
        if b < y:
            d['down_left'].add(item)
        elif y < b:
            d['down_right'].add(item)


def process_camel(x, y, n, arr):
    global d
    for item in arr:
        cat_quadrant(x, y, item)

    a = go_left_up(x + 1, y - 1, n)
    b = go_right_up(x + 1, y + 1, n)
    c = go_left_down(x - 1, y - 1)
    d = go_right_down(x - 1, y + 1, n)

    # print(a, b, c, d)
    return a + b + c + d


def maxKills(n, k, leader, r, c, array):
    leader = leader.upper()
    if leader == 'KING':
        return process_king(r, c, n, array)
    elif leader == 'KNIGHT':
        return process_horse(r, c, n, array)
    elif leader == 'BISHOP':
        return process_camel(r, c, n + 1, array)
    return -1


def my_main():
    n, k, leader = input().split()
    n = int(n)
    k = int(k)
    r, c = map(int, input().split())
    array = []
    for i in range(k):
        x, y = map(int, input().split())
        array.append((x, y))

    print(maxKills(n, k, leader, r, c, array))


if __name__ == '__main__':
    my_main()
