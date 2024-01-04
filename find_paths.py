from classes import *
from graph import graph

# node1 = Node(name='Урюпинск',  start_node=True, pass_time=1)
# node2 = Node(name='Самара', pass_time=1)
# node3 = Node(name='Перьм', pass_time=1)
# node4 = Node(name='Флоренция', pass_time=1, finish_node=True)


# edge1 = Edge(from_node=node1, to_node=node2, distance=280, static_speed=120)
# edge2 = Edge(from_node=node2, to_node=node3, distance=243, static_speed=60)
# edge3 = Edge(from_node=node3, to_node=node4, distance=245, static_speed=120)
# edge4 = Edge(from_node=node1, to_node=node4, distance=476, static_speed=90)


# graph = [[node1, node2, node3, node4], [edge1, edge2, edge3, edge4]]
# edges = graph[1]


# МАРШРУТЫ ИЗ УЗЛОВ
def find_all_paths(graph, start_node, finish_node, path=[], paths=[]):
    # Добавляем текущий узел в путь
    path = path + [start_node]

    # Если текущий узел - конечный, добавляем путь в список путей
    if start_node == finish_node:
        paths.append(path)

    # Рекурсивно ищем пути из каждого соседнего узла
    for edge in start_node.edges:
        if edge.to_node not in path:
            find_all_paths(graph, edge.to_node, finish_node, path, paths)

    return paths

start_node = next(node for node in graph[0] if node.start_node)
finish_node = next(node for node in graph[0] if node.finish_node)


# МАРШРУТЫ ИЗ СВЯЗЕЙ
def find_all_paths_edge(all_paths, edges):
    edges_path = []
    for path in all_paths:
        edge_path = []
        for i in range(len(path)-1):
            edge_path.append([edge for edge in edges if edge.from_node == path[i] and edge.to_node == path[i+1]][0])
        edges_path.append(edge_path)
    return edges_path




