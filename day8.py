from aocutil import file_input_line


def solve_day8(input_file_name):
    data = file_input_line(input_file_name, strip='\n')[0]
    image = []
    x = 25
    y = 6
    for i in range(0, len(data), x * y):
        temp = data[i: i + x * y]
        layer = []
        for pixel in temp:
            layer += [pixel]
        image.append(layer)

    fewest_0 = [float('inf'), '']
    for layer in image:
        count = layer.count('0')
        if count < fewest_0[0]:
            fewest_0 = [count, layer]

    result = fewest_0[1].count('1') * fewest_0[1].count('2')

    final = None
    image.reverse()
    for layer in image:
        if final is None:
            final = layer
        else:
            for i in range(x * y):
                if layer[i] != '2':
                    final[i] = layer[i]

    image = ''
    for i in range(0, len(final), x):
        temp = final[i: i + x]
        line = ''
        for pixel in temp:
            if pixel == '1':
                line += '█'
            else:
                line += ' '
        image += line + '\n'

    return result, image    # Use print(solve_day8()[1]) to see the message