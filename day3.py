from aocutil import file_input


def find_edges(wire):
    sum = 0
    edges = []
    head = (0, 0)
    for step in wire:
        dist = int(step[1:])
        dire = None
        if step[0] == 'L':
            dire = [-1, 0]
        if step[0] == 'R':
            dire = [1, 0]
        if step[0] == 'U':
            dire = [0, 1]
        if step[0] == 'D':
            dire = [0, -1]

        vect = [dire[0] * dist, dire[1] * dist]
        sum += abs(vect[0] + vect[1])
        head = [head[0] + vect[0], head[1] + vect[1], sum]
        edges.append(head)
    return edges


def intersect(l1, l2):
    l1pa = l1[0]
    l1pb = l1[1]
    l2pa = l2[0]
    l2pb = l2[1]

    try:
        r1 = (l1pa[0] - l1pb[0], l1pa[1] - l1pb[1]).index(0)
        r2 = (l2pa[0] - l2pb[0], l2pa[1] - l2pb[1]).index(0)
    except ValueError:
        return False, None

    if r1 == r2:
        return False, None

    if r1 > r2:
        meetup = (l2pa[r2], l1pa[r1])
    else:
        meetup = (l1pa[r1], l2pa[r2])
    if (min(l2pa, l2pb)[r1] <= meetup[r1] <= max(l2pa, l2pb)[r1]) and (min(l1pa, l1pb)[r2] <= meetup[r2] <= max(l1pa, l1pb)[r2]):
        return True, meetup,
    else:
        return False, None


def solve_day3(file_input_name):
    wire1, wire2 = file_input(file_input_name)
    wire1 = wire1.split(',')
    wire2 = wire2.split(',')

    edges1 = find_edges(wire1)
    edges2 = find_edges(wire2)
    prev1 = [0, 0, 0]
    prev2 = [0, 0, 0]

    intersection = []
    for point1 in edges1:
        for point2 in edges2:
            line1 = (prev1[:2], point1[:2])
            line2 = (prev2[:2], point2[:2])
            meetup = intersect(line1, line2)
            if meetup[0]:
                if meetup[1] != (0, 0):
                    intersection.append((abs(meetup[1][0]) + abs(meetup[1][1]), meetup[1], prev2[2] + prev1[2] + abs(line1[0][0] - line2[0][0]) + abs(line1[0][1] - line2[0][1])))
            prev2 = point2
        prev1 = point1
    return [min(intersection, key=lambda x: x[0])[0], min(intersection, key=lambda x: x[2])[2]]
