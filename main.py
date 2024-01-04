from classes import *
import random
from math import *
from graph import graph
from find_paths import *


# создание графа
node1 = Node(name='Светофор1',  start_node=True, pass_time=1)
node2 = Node(name='Светофор2', pass_time=1)
node3 = Node(name='Светофор3', pass_time=1)
node4 = Node(name='Светофор4', pass_time=1)

edge1 = Edge(from_node=node1, to_node=node2, distance=300, static_speed=11)
edge2 = Edge(from_node=node2, to_node=node3, distance=300, static_speed=11)
edge3 = Edge(from_node=node3, to_node=node4, distance=300, static_speed=11)
edge4 = Edge(from_node=node1, to_node=node4, distance=930, static_speed=33)

# укомплектованная карта
graph = [[node1, node2, node3, node4], [edge1, edge2, edge3, edge4]]

def sort_and_choice_edge(agent):
    # сортируем пути по весам
    edges = agent.position.edges
    sum_pheromons = sum([edge.pheromons for edge in edges])
    # создаем вероятности для кажого пути
    probability_edges = list(map(lambda edge: edge.set_probability(edge.pheromons / sum_pheromons), edges))
    # Выбор с учетом вероятности
    chosen_edge = random.choices(probability_edges, weights=[edge.probability for edge in probability_edges])[0]
    return chosen_edge

def moving(agent):
    chosen_edge = None
    # 2. Если агент на узле, выбираем оптимальный путь и перемещаем его туда
    if isinstance(agent.position, Node):
        chosen_edge = sort_and_choice_edge(agent)
        agent.move(chosen_edge)

        # 3 Добавляем в массив пути +1 объект
        chosen_edge.append_object(agent)

        # 4 изменяем скорость
        if len(chosen_edge.object_array) <= chosen_edge.count_obj_opt:
            chosen_edge.speed = chosen_edge.speed
        if chosen_edge.count_obj_max > len(chosen_edge.object_array) > chosen_edge.count_obj_opt:
            chosen_edge.speed = (1 - len(chosen_edge.object_array) / chosen_edge.count_obj_max)
        if len(chosen_edge.object_array) == chosen_edge.count_obj_max:
            chosen_edge.speed = 1

        # 5. Увеличение t(Счетчик определенного chosen_edge)
        agent.up_time(1)
        agent.summary_time += 1
    
        # 6 Если время агента достигло максимального времени нахождения на пути, то перемещяем его на узел, сбрасываем счетчик и удаляем из предыдущего пути
        if agent.time >= chosen_edge.time_max:
            agent.position.delete_object(agent)
            if len(chosen_edge.object_array) > chosen_edge.count_obj_opt:
                chosen_edge.up_pheromon((agent.value / agent.time)**(agent.time**-1))
            chosen_edge.up_pheromon(agent.value / agent.time)
            agent.summary_time += agent.time - agent.position.time_max
            agent.up_time(agent.time - agent.position.time_max, reboot=True)
            agent.move(agent.position.to_node)

            # 6.1 Если он достиг финиша, то удаляем его из списка объектов и прекращаем итерацию
            if agent.position.finish_node:
                agent.up_time(0, reboot=True)
                agent_array.remove(agent)

        # 7. Повторяем пункт 2
        if isinstance(agent.position, Node):
            chosen_edge = sort_and_choice_edge(agent)
            agent.move(chosen_edge)
            chosen_edge.append_object(agent)
        return None
    
    # Если агент на связи
    if isinstance(agent.position, Edge):
        agent.up_time(1)
        agent.summary_time += 1
        
        if agent.time >= agent.position.time_max:
            agent.position.delete_object(agent)
            if len(agent.position.object_array) > agent.position.count_obj_opt:
                agent.position.up_pheromon((agent.value / agent.time)**(agent.time**-1))
            agent.position.up_pheromon(agent.value / agent.time)
            agent.summary_time += agent.time - agent.position.time_max
            agent.up_time(agent.time - agent.position.time_max, reboot=True)

            if len(agent.position.object_array) <= agent.position.count_obj_opt:
                agent.position.speed = agent.position.speed
            if agent.position.count_obj_max > len(agent.position.object_array) > agent.position.count_obj_opt:
                agent.position.speed = (1 - len(agent.position.object_array) / agent.position.count_obj_max)
            if len(agent.position.object_array) == agent.position.count_obj_max:
                agent.position.speed = 1

            agent.move(agent.position.to_node)

            if agent.position.finish_node:
                agent.up_time(0, reboot=True)
                agent_array.remove(agent)

                
agent_array = set()
all_edges = graph[1]
# print(all_edges)

all_paths_nodes = find_all_paths(graph, node1, node4)
all_edge_path = find_all_paths_edge(all_paths_nodes, graph[1])

for path in all_paths_nodes:
    for node in path:
        print(node.name)
print(all_edge_path)

time = 0
static_traffic = 1
diff_time = 3
count_agent = 0
scale = 5

for __ in range(100_000):
    time += 1

    # Испарение
    edges_array = [edge.down_pheromon() for edge in all_edges]
    edges = [(f"{edge.name} count: {len(edge.object_array)} pheromons: {round(edge.pheromons, 2)}") for edge in edges_array]
    # print(f"{edges}\n")

    count_agent = int(scale * (sin(pi / (60 * diff_time) * time)) * static_traffic + (scale * static_traffic))

    # print(count_agent)
    for _ in range(count_agent):
        new_agent = Part(initial_position=node1, value=1)
        agent_array.add(new_agent)

    copy_agent_array = agent_array.copy()
    for agent in copy_agent_array:
        moving(agent)
        # if agent.id == 1:
        #     print(agent)
        # print(agent)
        
    
    all_paths_with_count_pheromon = []
    # сделаем красивый вывод данных
    print(f"\033[31mТекущее время: {time}")
    for path in all_edge_path:
        sum_pheromon = sum([edge.pheromons for edge in path])
        all_paths_with_count_pheromon.append(dict(key=[edge for edge in path], value=sum_pheromon))
    top_path = sorted(all_paths_with_count_pheromon, key=lambda path: path['value'])[-1]
    # print(top_path)
    print(f"\033[37mПуть {dict([(edge.from_node.name, edge.to_node.name) for edge in top_path['key']])}\nимеет {top_path['value']} феромонов\n")
    print('\n')

   

