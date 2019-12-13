from aocutil import file_input
# ran out of time. but at least hey, it answers part 1 :/


def solve_day12(data):
    moons = []
    for moon in data:
        moon = moon.replace(',', '').replace('=', '').replace('x', '').replace('y', '').replace('z', '').replace('<', '').replace('>', '')
        moon = moon.split()
        moon[0] = int(moon[0])
        moon[1] = int(moon[1])
        moon[2] = int(moon[2])
        moons.append([moon, [0, 0, 0]])

    energy_at_1000 = None
    starting = [[], [], [], []]
    ends = [0, 0, 0, 0]
    step = 0
    while True:
        # if step % 46867749 == 0:
        #     print(step)
        # if step == 0:
        #     for i in range(4):
        #         starting[i] = moons[i][0].copy()
        #     print(starting)
        # else:
        #     current = [[], [], [], []]
        #     for i in range(4):
        #         current[i] = moons[i][0].copy()
        #     for i in range(4):
        #         if starting[i] == current[i]:
        #             ends[i] = step
        #     try:
        #         ends.index(0)
        #     except ValueError:
        #         return ends

        for i in range(4):  # update velocity
            for j in range(4):
                if i != j:
                    gx = moons[i][0][0] - moons[j][0][0]
                    gy = moons[i][0][1] - moons[j][0][1]
                    gz = moons[i][0][2] - moons[j][0][2]
                    try:
                        moons[i][1][0] -= gx // abs(gx)
                    except ZeroDivisionError:
                        moons[i][1][0] += 0

                    try:
                        moons[i][1][1] -= gy // abs(gy)
                    except ZeroDivisionError:
                        moons[i][1][1] += 0

                    try:
                        moons[i][1][2] -= gz // abs(gz)
                    except ZeroDivisionError:
                        moons[i][1][2] += 0

        for i in range(4):  # update position
            moons[i][0][0] += moons[i][1][0]
            moons[i][0][1] += moons[i][1][1]
            moons[i][0][2] += moons[i][1][2]

        if step == 1000 - 1:
            total_energy = 0
            for moon in moons:
                pot = abs(moon[0][0]) + abs(moon[0][1]) + abs(moon[0][2])
                kin = abs(moon[1][0]) + abs(moon[1][1]) + abs(moon[1][2])
                total = pot * kin
                total_energy += total
            energy_at_1000 = total_energy
            print(energy_at_1000)
            return energy_at_1000
        step += 1


data = file_input('day12.txt', as_list=False)
print(solve_day12(data))
