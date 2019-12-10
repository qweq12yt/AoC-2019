from aocutil import file_input
from math import gcd
from copy import deepcopy


def solve_part1(input_file_name):
    data = file_input(input_file_name)
    asteroids = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == '#':
                asteroids.append((i, j))
    h = []
    for asteroid in asteroids:
        h.append(asteroids_in_range(asteroids, asteroid, data))
    return max(h, key=lambda x:x[0])[0]


def asteroids_in_range(asteroids, asteroid, data):
    to_return = [-1, None, None]
    temp = deepcopy(data)
    blind_spots = []
    for target in asteroids:
        if target != asteroid:
            var = (target[0] - asteroid[0], target[1] - asteroid[1])
            if var[0] != 0 or var[1] != 0:
                div = gcd(var[0], var[1])
                if div != 1:
                    var = (var[0] // div, var[1] // div)

                # DANGER, VERY STUPID CODE AHEAD
                n = 1
                flag = False
                while True:
                    try:
                        shadow = [asteroid[0] + var[0] * n, asteroid[1] + var[1] * n]
                        if shadow[0] >= 0 and shadow[1] >= 0:
                            if flag:
                                temp[shadow[0]][shadow[1]] = 'x'
                                if tuple(shadow) not in blind_spots:
                                    blind_spots.append(tuple(shadow))
                            if temp[shadow[0]][shadow[1]] == '#':
                                flag = True
                        else:
                            break
                        n += 1
                    except IndexError:
                        break
                # I told you :/

    visible = len(set(asteroids) - set(blind_spots)) - 1
    to_return[0] = visible
    to_return[1] = [asteroid[1], asteroid[0]]
    to_return[2] = set(asteroids) - set(blind_spots)

    return to_return   # [0] is the quantity, [1] is what asteroid is the chosen one. [2] is a set of all VISIBLE asteroids