import maps
import common
import adjacency as adj


def map_the_merged_graph_in_architecture_manually(h_vertices: list, h_edges: list, m_vertices: list, m_edges: list):
    h_adjacency_preset = adj.get_adjacency_list_for_hexagonal_architecture(h_vertices, h_edges)
    print(h_adjacency_preset)

    equivalence, graph_nodes = maps.take_corresponding_nodes_for_merged_graph_in_architecture(m_vertices)
    h_edges_given = maps.create_edges_in_architecture_according_to_graph(m_edges, equivalence)

    edges_not_violated, edges_violated = maps.find_which_edges_are_violating_adjacency(h_edges_given, h_adjacency_preset)
    locked_paths, locked_swaps = maps.get_all_shortest_paths_for_violated_edges(edges_violated, h_adjacency_preset, h_vertices)
    graph_edges = maps.get_all_paths_for_merged_graph_with_final_weights(edges_not_violated, locked_paths, locked_swaps, edges_violated)

    node_color_map, edge_color_map, h_weighted_edges = maps.get_color_for_plotting_in_architecture(h_vertices, graph_nodes, h_edges, graph_edges)
    initial_cost, additional_cost, total_cost = maps.get_costs(m_edges, locked_swaps)

    print(f"Total Number of Swaps for This Plotting is: {common.calculate_total_violations(locked_swaps)}")
    print(f"Total Cost For This Graph is {total_cost}")
    print(f"Initial Cost For This Graph was {initial_cost}")
    print(f"Additional Cost For This Graph is {additional_cost}")

    return h_weighted_edges, node_color_map, edge_color_map



