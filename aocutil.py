def file_input(file_name, key=str):
    file = open(file_name, 'r')
    data = []
    for line in file:
        data.append(key(line.strip('\n')))
    return data