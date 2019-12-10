from aocutil import file_input
from math import gcd, atan, degrees
from copy import deepcopy


def get_angle(center, target):
    target = list(target)
    target[0] -= center[0]
    target[1] -= center[1]
    try:
        angle = degrees(atan(target[0] / target[1]))
    except ZeroDivisionError:
        if target[0] > 0:
            return 90
        else:
            return -90 + 360
    if angle < 0:
        return angle + 360
    else:
        return angle


def to_clockwise(angle):
    angle -= 270
    if angle < 0:
        return angle + 360
    return angle


def solve_day10(input_file_name):
    data = file_input(input_file_name)
    asteroids = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == '#':
                asteroids.append((i, j))
    h = []
    for asteroid in asteroids:
        h.append(asteroids_in_range(asteroids, asteroid, data))
    part1, station, asteroids = max(h, key=lambda x: x[0])
    clockwise = []
    for asteroid in asteroids:
        clockwise.append((list(reversed(asteroid)), to_clockwise(get_angle(station, asteroid))))
    clockwise.sort(key=lambda x: x[1])

    # return part1, list(list(clockwise[10 -1][0]).__reversed__()), station
    return part1


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

    to_return[1] = [asteroid[0], asteroid[1]]   # (y, x)
    to_return[2] = set(asteroids) - set(blind_spots)
    to_return[2].remove(tuple(to_return[1]))
    to_return[0] = len(to_return[2])

    return to_return   # [0] is the quantity, [1] is what asteroid is the chosen one. [2] is a set of all VISIBLE asteroids


print(solve_day10('day10.txt'))

