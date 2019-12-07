# Because stupidity, adapting the intcode thingy to asyncio snowballed into something long, might as well start from the
# beginning, so instead of doing that now, i will only have part 1 solvable, as that doesn't need it
# I'm so fucking dumb :/

from aocutil import file_input_line
from itertools import permutations


def calculate_signal_ab(initial, inputs):
    data = initial.copy()
    ipointer = 0
    output = []
    input = inputs
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
            n = input.pop(0)
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

            output.append(data[p1])
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

    return output[0]    # fix for later uses


def calculate_signal_thrusters(initial):
    settings = permutations([0,1,2,3,4])
    outputs = []
    for setting in settings:
        output = [0, None, None, None, None, None]
        for i in range(1, len(output)):
            data = initial.copy()
            output[i] = calculate_signal_ab(data, [setting[i - 1], output[i - 1]])
        outputs.append(output[-1])
    return max(outputs)


data = file_input_line('day7.txt', ',', int, '\n')
print(calculate_signal_thrusters(data))