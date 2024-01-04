class Edge:
    next_id = 1

    def __init__(self, from_node, to_node, distance, static_speed):
        # BASE PARAMETRS
        self.distance = distance
        self.static_speed = static_speed
        self.distance_between = 2
        self.average_car_length = 4.53

        self.from_node = from_node
        self.to_node = to_node
        self.name = f"{self.from_node.name} -> {self.to_node.name}"
        self.id = self.next_id
        Edge.next_id += 1

        # VARIBLE PARAMETRS
        self.pheromons = 1
        self.object_array = []
        self.count_obj_max = int(self.distance / (self.distance_between + self.average_car_length))
        self.count_obj_opt = int((self.to_node.pass_time * static_speed) / (self.distance_between + self.average_car_length))

        self.speed = static_speed

        self.time_max = self.distance / self.speed 
        self.probability = None

        from_node.add_edge(self)

    def set_probability(self, value):
        self.probability = value
        return self
    
    def up_pheromon(self, count):
        self.pheromons += count
    
    def down_pheromon(self):
        self.pheromons -= self.pheromons * 0.4
        return self
    
    def delete_object(self, obj):
        if obj in self.object_array:
            self.object_array.remove(obj)

    def append_object(self, obj):
        self.object_array.append(obj)

    def __str__(self):
        # return f"{self.from_node.name} -> {self.to_node.name}"
        return self.name

class Node:
    next_id = 1
    def __init__(self, pass_time, name = None, position = None, start_node = None, finish_node = None,):
        self.pass_time = pass_time
        self.id = self.next_id
        Node.next_id += 1
        self.name = name
        self.position = position
        self.edges = []
        self.start_node = start_node
        self.finish_node = finish_node

    def add_edge(self, edge):
        if isinstance(edge, Edge):
            self.edges.append(edge)
        else:
            raise TypeError("Edge must be an instance of the Edge class.")

    def __str__(self):
        return self.name
    
    def get_data(self):
        return f"Node: {self.name}, Position: {self.position}, Edges: {[edge.to_node.name for edge in self.edges]}"

class Part():
    next_id = 1

    def __init__(self, initial_position = Node, value = 1, position_node = None, position_edge = None):
        # BASE PARAMETRS
        self.id = self.next_id
        self.length = 4.53
        self.distance_between = 2

        Part.next_id += 1
        if isinstance(initial_position, Node):
            self.initial_position = initial_position
        else:
            self.initial_position = None
        self.position = initial_position
        self.value = value
        self.edges_variant = self.position.edges
        self.time = 0
        self.summary_time = 0
        
    
    def up_time(self, value, reboot=None):
        self.time += value
        if reboot:
            self.time = value
        return self
    
    def move(self, position):
        # Сделать ограничения на ввод данных
        self.position = position
        if isinstance(position, Node):
            self.edges_variant = position.edges
        if isinstance(position, Edge):
            self.edges_variant = position.to_node
        return self
    
    def __str__(self):
        if isinstance(self.position, Edge):
            return f"id:{self.id} Текущая позиция: {self.position}, Значение: {self.value}, Возможные пути: {self.edges_variant}, time: {self.time}, summary_time: {self.summary_time}"
        return f"id:{self.id} Текущая позиция: {self.position}, Значение: {self.value}, Возможные пути: {[variant.name for variant in self.edges_variant]}, time: {self.time}, summary_time: {self.summary_time}"

