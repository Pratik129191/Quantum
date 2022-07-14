def find_index_of_largest_graph(graphs: list, locked_edges: list):
    largest_graph = len(locked_edges[0])
    index = 0
    for g in range(0, len(graphs)):
        if largest_graph < len(locked_edges[g]):
            largest_graph = len(locked_edges[g])
            index = g
    return index


def merge_all_graphs(graphs, locked_edges, locked_vertices, positions, node_color_maps: list):
    index = find_index_of_largest_graph(graphs, locked_edges)
    m_vertices = locked_vertices[index]
    previous = locked_edges[index]
    node_color_map = node_color_maps[index]
    new = []

    for g in range(0, len(graphs)):
        if g != index:
            for edge in locked_edges[g]:
                if edge not in previous + new:
                    new.append(edge)
                    if edge[0] not in m_vertices:
                        m_vertices.append(edge[0])
                        node_color_map.append('BLUE')
                    if edge[1] not in m_vertices:
                        m_vertices.append(edge[1])
                        node_color_map.append('BLUE')

    m_edges = previous + new
    return previous, new, m_vertices, m_edges, node_color_map






