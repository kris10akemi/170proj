import networkx as nx
import os

small = 7
medium = 22
large = 31

def small_output():
    
    graph = nx.Graph()
    num_students = small * small
    num_buses = small

    students = []
    for i in range(49):
        students.append(i + 1)

    graph.add_nodes_from(students)

    print(list(graph.nodes))



def main():
    '''
        Main method which iterates over all inputs and calls `solve` on each.
        The student should modify `solve` to return their solution and modify
        the portion which writes it to a file to make sure their output is
        formatted correctly.
    '''
    small_output()

if __name__ == '__main__':
    main()


