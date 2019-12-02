"""Loads a file and returns every single line as a entry in a array"""


def file_input(file_name, key=str):
    file = open(file_name, 'r')
    data = []
    for line in file:
        data.append(key(line.strip('\n')))
    return data


"""Loads a file and returns the first line separated according to the parameter sep"""


def file_input_line(file_name, sep=' ', key=str):
    file = open(file_name, 'r').readline()
    data = []
    file = file.split(sep)
    for item in file:
        data.append(key(item))
    return data