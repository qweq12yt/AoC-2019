from aocutil import file_input_line


def solve(initial, k, j):
        data = initial.copy()
        data[1], data[2] = k, j
        for i in range(0, len(data), 4):
            opc = data[i]
            if opc == 99:
                break

            elif opc == 1:
                a = data[i + 1]
                b = data[i + 2]
                c = data[i + 3]

                data[c] = data[a] + data[b]

            elif opc == 2:
                a = data[i + 1]
                b = data[i + 2]
                c = data[i + 3]

                data[c] = data[a] * data[b]

            else:
                break
        return data


def solve_part1(input_file_name):
    data = file_input_line(input_file_name, ',', int)
    return solve(data, 12, 2)[0]


def solve_part2(input_file_name):
    data = file_input_line(input_file_name, ',', int)
    for i in range(100):
        for j in range(100):
            r = solve(data, i, j)
            if r[0] == 19690720:
                return 100 * r[1] + r[2]
