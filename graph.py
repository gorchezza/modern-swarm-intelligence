from classes import *

node1 = Node(name='Урюпинск',  start_node=True, pass_time=1)
node2 = Node(name='Самара', pass_time=1)
node3 = Node(name='Перьм', pass_time=1)
node4 = Node(name='Флоренция', pass_time=1, finish_node=True)
# node5 = Node(name='Казань', pass_time=1)


edge1 = Edge(from_node=node1, to_node=node2, distance=300, static_speed=11)
edge2 = Edge(from_node=node2, to_node=node3, distance=300, static_speed=11)
edge3 = Edge(from_node=node3, to_node=node4, distance=300, static_speed=11)
edge4 = Edge(from_node=node1, to_node=node4, distance=200, static_speed=11)
# edge5 = Edge(from_node=node1, to_node=node5, distance=300, static_speed=11)

graph = [[node1, node2, node3, node4], [edge1, edge2, edge3, edge4]]
edges = graph[1]
# print(graph)


# node1 = Node(name='Урюпинск',  start_node=True, pass_time=1)
# node2 = Node(name='Самара', pass_time=1)
# node3 = Node(name='Перьм', pass_time=1)
# node4 = Node(name='Флоренция', pass_time=1)
# node5 = Node(name='1', pass_time=1)
# node6 = Node(name='2', finish_node=True, pass_time=1)

# edge1 = Edge(from_node=node1, to_node=node2, distance=280, static_speed=120)
# edge2 = Edge(from_node=node2, to_node=node3, distance=243, static_speed=60)
# edge3 = Edge(from_node=node3, to_node=node4, distance=245, static_speed=120)
# edge4 = Edge(from_node=node1, to_node=node4, distance=476, static_speed=90)
# edge5 = Edge(from_node=)