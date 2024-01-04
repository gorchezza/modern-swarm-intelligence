# from classes import * 
# import random

# node1 = Node(name='Урюпинск',  start_node=True, pass_time=2)
# node2 = Node(name='Самара', pass_time=2)
# node3 = Node(name='Перьм', pass_time=2)
# node4 = Node(name='Флоренция', pass_time=2, finish_node=True)


# edge1 = Edge(from_node=node1, to_node=node2, distance=300, static_speed=11)
# edge2 = Edge(from_node=node2, to_node=node3, distance=300, static_speed=11)
# edge3 = Edge(from_node=node3, to_node=node4, distance=300, static_speed=11)
# edge4 = Edge(from_node=node1, to_node=node4, distance=200, static_speed=11)


# # def sort_and_choice_edge(agent):
# #     # сортируем пути по весам
# #     edges = agent.position.edges
# #     sum_pheromons = sum([edge.pheromons + 1 for edge in edges])
# #     # создаем вероятности для кажого пути
# #     probability_edges = list(map(lambda edge: edge.set_probability(edge.pheromons + 1 / sum_pheromons), edges))
# #     # Выбор с учетом вероятности
# #     chosen_edge = random.choices(probability_edges, weights=[edge.probability for edge in probability_edges])[0]
# #     print([edge.probability for edge in probability_edges])
# #     return chosen_edge

# for __ in range(5):
#     agent = Part(initial_position=node1, value=1)
#     agent.move(edge4)
#     agent.position.append_object(agent)
#     if len(agent.position.object_array) <= agent.position.count_obj_opt:
#         agent.position.speed = agent.position.speed
#     if agent.position.count_obj_max > len(agent.position.object_array) > agent.position.count_obj_opt:
#         agent.position.speed = (1 - len(agent.position.object_array) / agent.position.count_obj_max)
#     if len(agent.position.object_array) == agent.position.count_obj_max:
#         agent.position.speed = 1

# print(len(edge4.object_array))
# print(agent.position.count_obj_opt)
# print(agent.position.count_obj_max)

# print(edge4.speed)
# print(edge4.time_max)

# print("\n")

# for __ in range(1):
#     agent = Part(initial_position=node1, value=1)
#     agent.move(edge1)
#     agent.position.append_object(agent)
#     if len(agent.position.object_array) <= agent.position.count_obj_opt:
#         agent.position.speed = agent.position.speed
#     if agent.position.count_obj_max > len(agent.position.object_array) > agent.position.count_obj_opt:
#         agent.position.speed = (1 - len(agent.position.object_array) / agent.position.count_obj_max)
#     if len(agent.position.object_array) == agent.position.count_obj_max:
#         agent.position.speed = 1

# print(len(edge1.object_array))
# print(agent.position.count_obj_opt)
# print(agent.position.count_obj_max)
# print(edge1.speed)
# print(edge1.time_max)