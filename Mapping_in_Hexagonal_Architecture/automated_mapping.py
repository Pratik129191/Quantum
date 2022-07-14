import adjacency as adj
import common
import maps


def is_equivalence_unique(equivalence: list, global_equivalence: list):
    if equivalence in global_equivalence:
        return False
    return True


def map_the_merged_graph_into_architecture_automatically(h_vertices: list, h_edges: list, m_vertices: list, m_edges: list, equivalence: list, graph_nodes: list):
    h_adjacency_preset = adj.get_adjacency_list_for_hexagonal_architecture(h_vertices, h_edges)

    h_edges_given = maps.create_edges_in_architecture_according_to_graph(m_edges, equivalence)

    edges_not_violated, edges_violated = maps.find_which_edges_are_violating_adjacency(h_edges_given, h_adjacency_preset)
    locked_paths, locked_swaps = maps.get_all_shortest_paths_for_violated_edges(edges_violated, h_adjacency_preset, h_vertices)
    graph_edges = maps.get_all_paths_for_merged_graph_with_final_weights(edges_not_violated, locked_paths, locked_swaps, edges_violated)

    node_color_map, edge_color_map, h_weighted_edges = maps.get_color_for_plotting_in_architecture(h_vertices, graph_nodes, h_edges, graph_edges)
    initial_cost, additional_cost, total_cost = maps.get_costs(m_edges, locked_swaps)

    total_violations = common.calculate_total_violations(locked_swaps)
    return h_weighted_edges, node_color_map, edge_color_map, total_violations, equivalence, total_cost, additional_cost, initial_cost


def perform_mapping_automatically(h_vertices: list, h_edges: list, m_vertices: list, m_edges: list, max_loop=100):
    essentials = {}
    global_equivalence = []
    equivalence, graph_nodes = maps.initialize_corresponding_nodes_for_merged_graph_in_architecture(h_vertices, m_vertices)
    global_equivalence.append(equivalence)

    for i in range(1, max_loop + 1):
        if i > 1:
            if is_equivalence_unique(equivalence, global_equivalence):
                temp = []
                h_weighted_edges, node_color_map, edge_color_map, total_violations, equivalence_mapping, total_cost, additional_cost, initial_cost = \
                    map_the_merged_graph_into_architecture_automatically(
                        h_vertices, h_edges, m_vertices, m_edges, equivalence, graph_nodes
                    )

                temp.append(h_weighted_edges)
                temp.append(node_color_map)
                temp.append(edge_color_map)
                temp.append(total_violations)
                temp.append(equivalence_mapping)
                temp.append(total_cost)
                temp.append(additional_cost)
                temp.append(initial_cost)

                essentials[i] = temp
            else:
                equivalence, graph_nodes = maps.initialize_corresponding_nodes_for_merged_graph_in_architecture(h_vertices, m_vertices)
                global_equivalence.append(equivalence)
                temp = []
                h_weighted_edges, node_color_map, edge_color_map, total_violations, equivalence_mapping, total_cost, additional_cost, initial_cost = \
                    map_the_merged_graph_into_architecture_automatically(
                        h_vertices, h_edges, m_vertices, m_edges, equivalence, graph_nodes
                    )

                temp.append(h_weighted_edges)
                temp.append(node_color_map)
                temp.append(edge_color_map)
                temp.append(total_violations)
                temp.append(equivalence_mapping)
                temp.append(total_cost)
                temp.append(additional_cost)
                temp.append(initial_cost)

                essentials[i] = temp

    all_violations = common.get_all_violations_for_every_plotting(essentials)
    minimum_violations, lowest = common.find_minimum_violations_and_corresponding_plotting(all_violations, essentials)

    global_equivalence.clear()
    return essentials, minimum_violations, lowest



