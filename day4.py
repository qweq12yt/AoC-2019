from aocutil import file_input_line
from itertools import product


def has_doubles(password):
    for char in '0123456789':
        if password.count(char) == 2:
            return True
    return False


def has_repetitions(password):
    for char in '0123456789':
        if password.count(char) >= 2:
            return True
    return False


def never_decreases(password):
    prev = -1
    for char in password:
        if int(char) >= prev:
            prev = int(char)
        else:
            return False
    return True


def solve_day4(file_input_name):
    limit = file_input_line(file_input_name, '-', int)
    passwords1 = []
    passwords2 = []
    for password in product('0123456789', repeat=6):
        temp = ''
        for char in password:
            temp += char
        if limit[0] <= int(temp) <= limit[1] and never_decreases(temp) and has_repetitions(temp):
            passwords1.append(temp)
            if has_doubles(temp):
                passwords2.append(temp)

    return len(passwords1), len(passwords2)
