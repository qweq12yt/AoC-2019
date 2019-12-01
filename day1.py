from aocutil import file_input

"""Solves the day 1 puzzle for Advent of Code 2019"""


def solve_day1(input_file_name):
    data = file_input(input_file_name, int)
    part1 = 0
    part2 = 0
    for mass in data:
        fuel = int(mass / 3) - 2
        part1 += fuel
        part2 += fuel
        while fuel > 0:
            fuel = int(fuel / 3) - 2
            if fuel < 0:
                fuel = 0
            part2 += fuel

    print(part1)
    print(part2)
    return part1, part2