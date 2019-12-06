from aocutil import file_input
import networkx as nx
# I was too lazy to make my own structures and algorithms so yeah im using a library :3
# All hail Dijkstra


def solve_day6(input_file_name):
    graph = nx.Graph()
    data = file_input(input_file_name)
    for line in data:
        temp = line.split(')')
        graph.add_edge(temp[0], temp[1])

    paths = nx.single_source_shortest_path_length(graph, 'COM')
    sum = 0     # part 1
    for key in paths:
        sum += paths[key]
    to_santa = nx.shortest_path_length(graph, 'YOU', 'SAN') - 2     # Part 2
    return sum, to_santa