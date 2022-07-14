import networkx as nx
import matplotlib.pyplot as plt


def draw_graphs(graphs: list, locked_edges: list, locked_vertices: list, positions: list, node_color_maps: list):
    for g in range(0, len(graphs)):
        qg = nx.Graph()
        qg.add_nodes_from(locked_vertices[g])
        qg.add_weighted_edges_from(locked_edges[g])
        weight = nx.get_edge_attributes(qg, 'weight')
        nx.draw_networkx_edge_labels(qg, pos=positions[g], edge_labels=weight)
        nx.draw_networkx(qg, pos=positions[g], with_labels=True, node_color=node_color_maps[g])
        plt.figure(g)
    plt.show()
    input("Press Enter To Continue ...")


def get_edge_colors_for_merged_graph(previous: list, new: list):
    color = []
    for edge in previous + new:
        if edge in previous:
            color.append('black')
        else:
            color.append('red')
    return color


def draw_merged_graph(previous: list, new: list, vertices: list, node_color_map: list):
    colors = get_edge_colors_for_merged_graph(previous, new)
    qmg = nx.Graph()
    qmg.add_nodes_from(vertices)
    qmg.add_weighted_edges_from(previous + new)
    weights = nx.get_edge_attributes(qmg, 'weight')
    pos = nx.shell_layout(qmg)
    nx.draw_networkx_edge_labels(qmg, pos=pos, edge_labels=weights)
    nx.draw_networkx(qmg, pos=pos, with_labels=True, edge_color=colors, node_color=node_color_map)
    plt.show()
    input("Press Enter To Continue...")


def draw_hexagonal_architecture(vertices: list, positions: dict, edges: list):
    qg = nx.Graph()
    qg.add_nodes_from(vertices)
    qg.add_weighted_edges_from(edges)
    weights = nx.get_edge_attributes(qg, 'weight')
    nx.draw_networkx_edge_labels(qg, pos=positions, edge_labels=weights)
    nx.draw_networkx(qg, pos=positions, with_labels=True, node_size=1000, width=4)
    plt.show()


def draw_hexagonal_architecture_with_mapping(vertices: list, positions: dict, edges: list, edge_color_maps: list,
                                             node_color_maps: list):
    qg = nx.Graph()
    qg.add_nodes_from(vertices)
    qg.add_weighted_edges_from(edges)
    weights = nx.get_edge_attributes(qg, 'weight')
    for w in weights:
        if isinstance(weights[w], int):
            weights[w] = 'O'
    nx.draw_networkx_edge_labels(qg, pos=positions, edge_labels=weights)
    nx.draw_networkx(qg, pos=positions, with_labels=True, node_size=1000, node_color=node_color_maps,
                     edge_color=edge_color_maps)
    plt.show()


# noinspection PySimplifyBooleanCheck
def draw_hexagonal_architecture_with_mapping_for_automated_one(vertices: list, positions: dict, edges: list,
                                                               edge_color_maps: list, node_color_maps: list,
                                                               equivalence_mapping: list):
    qmg = nx.Graph()
    nodes = []
    pos = {}
    i = 1
    for e in equivalence_mapping:
        nodes.append(e[0])
        nodes.append(e[1])
        pos[e[0]] = [1, i]
        pos[e[1]] = [4, i]
        i += 1

    qmg.add_nodes_from(nodes)
    qmg.add_edges_from(equivalence_mapping)
    plt.figure(1)
    nx.draw_networkx(qmg, pos=pos, with_labels=True, node_size=1000)

    qg = nx.Graph()
    qg.add_nodes_from(vertices)
    qg.add_weighted_edges_from(edges)
    weights = nx.get_edge_attributes(qg, 'weight')
    for w in weights:
        if isinstance(weights[w], int):
            weights[w] = 'O'
    plt.figure(2)
    nx.draw_networkx_edge_labels(qg, pos=positions, edge_labels=weights)
    nx.draw_networkx(qg, pos=positions, with_labels=True, node_size=1000, node_color=node_color_maps,
                     edge_color=edge_color_maps)

    plt.show()
