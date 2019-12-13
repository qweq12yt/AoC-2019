"""Loads a file and returns every single line as a entry in a array"""


def file_input(file_name, key=str, as_list=True):
    file = open(file_name, 'r')
    data = []
    if as_list:
        for line in file:
            l = []
            for char in line:
                if char != '\n':
                    l.append(key(char))
            data.append(l)
    else:
        for line in file:
            data.append(line.strip('\n'))
    return data.copy()


"""Loads a file and returns the first line separated according to the parameter sep"""


def file_input_line(file_name, sep=' ', key=str, strip=''):
    file = open(file_name, 'r').readline().strip(strip)
    data = []
    file = file.split(sep)
    for item in file:
        data.append(key(item))
    return data.copy()


"""Prints any 2d grid (matrix). Good for debuging!"""


def print_grid(grid):
    string = ''
    for line in grid:
        l = ''
        for char in line:
            l += str(char)
        string += l + '\n'
    print(string)