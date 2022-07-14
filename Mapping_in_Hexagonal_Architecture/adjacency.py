def find_all_neighbours_of_this_vertex(vertex, edges: list):
    neighbours = []
    for edge in edges:
        if edge[0] == vertex:
            if edge[1] not in neighbours:
                neighbours.append(edge[1])
        if edge[1] == vertex:
            if edge[0] not in neighbours:
                neighbours.append(edge[0])
    return neighbours


def get_adjacency_list_for_merged_graph(vertices: list, edges: list):
    adjacency = {}
    for v in vertices:
        if v not in adjacency:
            adjacency[v] = find_all_neighbours_of_this_vertex(v, edges)
    return adjacency


def get_adjacency_list_for_hexagonal_architecture(vertices: list, edges: list):
    adjacency = {}
    for v in vertices:
        if v not in adjacency:
            adjacency[v] = find_all_neighbours_of_this_vertex(v, edges)
    return adjacency

