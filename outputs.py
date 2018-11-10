import networkx as nx
import os
import matplotlib.pyplot as plt
import sys

small = 7
medium = 22
large = 31

size = None

def small_output():
    
    graph = nx.Graph()
    num_students = small * small
    num_buses = small

    students = []
    for i in range(num_students):
        students.append(i + 1)

    graph.add_nodes_from(students)

    student = 1
    while student <= num_students:
        for i in range(student, student + small):
            for k in range(student, student + small):
                if i != k:
                    graph.add_edge(i, k)
        student += small

    # print(list(graph.nodes))

    # play around with k and iterations - more iterations = centered around component, k = optimal node dist
    pos=nx.spring_layout(graph, k = .9, iterations = 70)
    nx.draw(graph, pos, node_size = 25, font_size = 8, with_labels=True)
    plt.show()

def output(size):
    
    graph = nx.Graph()
    num_students = size * size
    num_buses = size

    students = []
    for i in range(num_students):
        students.append(i + 1)

    graph.add_nodes_from(students)

    student = 1
    while student <= num_students:
        for i in range(student, student + size):
            for k in range(student, student + size):
                if i != k:
                    graph.add_edge(i, k)
        student += size

    # print(list(graph.nodes))

    # play around with k and iterations - more iterations = centered around component, k = optimal node dist
    pos=nx.spring_layout(graph, k = .9, iterations = 70)
    nx.draw(graph, pos, node_size = 25, font_size = 8, with_labels=True)
    plt.show()

if __name__ == '__main__':
    size = int(sys.argv[1])
    if size != None:
        output(size)
    # small_output()


