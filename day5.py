from aocutil import file_input_line

# This must be the MOST idiotic solution, but i was too tired to do a tidy and readable code
# so deal with it, i might come back to this after AoC is done or i feel like it


def solve_part1(initial):
    data = initial.copy()
    ipointer = 0
    while True:
        temp = str(data[ipointer])
        while len(temp) < 5:
            temp = '0' + temp

        modes = temp[:3]
        opc = int(temp[3:])

        a = int(modes[2])
        b = int(modes[1])
        c = int(modes[0])
        p1, p2, p3 = None, None, None

        if opc == 99:
            break

        elif opc == 1:
            if a == 0:
                p1 = data[ipointer + 1]
                p1 = data[p1]
            else:
                p1 = ipointer + 1
                p1 = data[p1]

            if b == 0:
                p2 = data[ipointer + 2]
                p2 = data[p2]
            else:
                p2 = ipointer + 2
                p2 = data[p2]

            if c == 0:
                p3 = data[ipointer + 3]
            else:
                p3 = ipointer + 3

            data[p3] = p1 + p2

            ipointer += 4

        elif opc == 2:
            if a == 0:
                p1 = data[ipointer + 1]
                p1 = data[p1]
            else:
                p1 = ipointer + 1
                p1 = data[p1]

            if b == 0:
                p2 = data[ipointer + 2]
                p2 = data[p2]
            else:
                p2 = ipointer + 2
                p2 = data[p2]

            if c == 0:
                p3 = data[ipointer + 3]
            else:
                p3 = ipointer + 3

            data[p3] = p1 * p2

            ipointer += 4

        elif opc == 3:
            n = int(input('input time: '))
            if a == 0:
                p1 = data[ipointer + 1]
            else:
                p1 = ipointer + 1

            data[p1] = n

            ipointer += 2

        elif opc == 4:
            if a == 0:
                p1 = data[ipointer + 1]
            else:
                p1 = ipointer + 1

            print(data[p1])
            ipointer += 2

        else:
            raise Exception('Invalid opcode')

    return data


def solve_part2(initial):
    data = initial.copy()
    ipointer = 0
    while True:
        temp = str(data[ipointer])
        while len(temp) < 5:
            temp = '0' + temp

        modes = temp[:3]
        opc = int(temp[3:])

        a = int(modes[2])
        b = int(modes[1])
        c = int(modes[0])

        p1, p2, p3 = None, None, None

        if opc == 99:
            break

        # Add
        elif opc == 1:
            if a == 0:
                p1 = data[ipointer + 1]
                p1 = data[p1]
            else:
                p1 = ipointer + 1
                p1 = data[p1]

            if b == 0:
                p2 = data[ipointer + 2]
                p2 = data[p2]
            else:
                p2 = ipointer + 2
                p2 = data[p2]

            if c == 0:
                p3 = data[ipointer + 3]
            else:
                p3 = ipointer + 3

            data[p3] = p1 + p2

            ipointer += 4

        # Mult
        elif opc == 2:
            if a == 0:
                p1 = data[ipointer + 1]
                p1 = data[p1]
            else:
                p1 = ipointer + 1
                p1 = data[p1]

            if b == 0:
                p2 = data[ipointer + 2]
                p2 = data[p2]
            else:
                p2 = ipointer + 2
                p2 = data[p2]

            if c == 0:
                p3 = data[ipointer + 3]
            else:
                p3 = ipointer + 3

            data[p3] = p1 * p2

            ipointer += 4

        # In
        elif opc == 3:
            n = int(input('input time: '))
            if a == 0:
                p1 = data[ipointer + 1]
            else:
                p1 = ipointer + 1

            data[p1] = n

            ipointer += 2

        # Out
        elif opc == 4:
            if a == 0:
                p1 = data[ipointer + 1]
            else:
                p1 = ipointer + 1

            print(data[p1])
            ipointer += 2

        # Jump if true
        elif opc == 5:
            if a == 0:
                p1 = data[ipointer + 1]
                p1 = data[p1]
            else:
                p1 = ipointer + 1
                p1 = data[p1]

            if b == 0:
                p2 = data[ipointer + 2]
                p2 = data[p2]
            else:
                p2 = data[ipointer + 2]

            if p1 != 0:
                ipointer = p2
            else:
                ipointer += 3

        # Jump if false
        elif opc == 6:
            if a == 0:
                p1 = data[ipointer + 1]
                p1 = data[p1]
            else:
                p1 = ipointer + 1
                p1 = data[p1]

            if b == 0:
                p2 = data[ipointer + 2]
                p2 = data[p2]
            else:
                p2 = data[ipointer + 2]

            if p1 == 0:
                ipointer = p2
            else:
                ipointer += 3

        # Less than
        elif opc == 7:
            if a == 0:
                p1 = data[ipointer + 1]
                p1 = data[p1]
            else:
                p1 = ipointer + 1
                p1 = data[p1]

            if b == 0:
                p2 = data[ipointer + 2]
                p2 = data[p2]
            else:
                p2 = ipointer + 2
                p2 = data[p2]

            if c == 0:
                p3 = data[ipointer + 3]
            else:
                p3 = ipointer + 3

            if p1 < p2:
                data[p3] = 1
            else:
                data[p3] = 0

            ipointer += 4

        # Equal to
        elif opc == 8:
            if a == 0:
                p1 = data[ipointer + 1]
                p1 = data[p1]
            else:
                p1 = ipointer + 1
                p1 = data[p1]

            if b == 0:
                p2 = data[ipointer + 2]
                p2 = data[p2]
            else:
                p2 = ipointer + 2
                p2 = data[p2]

            if c == 0:
                p3 = data[ipointer + 3]
            else:
                p3 = ipointer + 3

            if p1 == p2:
                data[p3] = 1
            else:
                data[p3] = 0

            ipointer += 4

        else:
            raise Exception('Invalid opcode')

    return data


data = file_input_line('day5.txt', ',', int, '\n')

solve_part1(data)
solve_part2(data)