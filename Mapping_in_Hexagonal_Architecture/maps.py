import common as com
import available_paths as ap
import maps


def convert_to_int(x: str):
    if x == '':
        return 0
    else:
        return int(x)


def initialize_corresponding_nodes_for_merged_graph_in_architecture(h_vertices: list, m_vertices: list):
    points = com.initialize_vertex_points_for_merged_graph(m_vertices, h_vertices)
    h_nodes = com.create_vertex_names_from_random_points(points)
    equivalence = com.get_equivalence_points_for_plotting_graph(m_vertices, h_nodes)

    return equivalence, h_nodes


def take_corresponding_nodes_for_merged_graph_in_architecture(m_vertices: list):
    equivalence = []
    h_nodes = []
    for m in m_vertices:
        h = input(f"Enter The Corresponding Node for {m} in Architecture:\t").upper()
        temp = (h, m)
        h_nodes.append(h)
        equivalence.append(temp)
    return equivalence, h_nodes


def create_edges_in_architecture_according_to_graph(m_edges: list, equivalence: list):
    h_edges_given = []

    for me in m_edges:
        q1 = com.get_corresponding_h_node_for_q_bit(me[0], equivalence)
        q2 = com.get_corresponding_h_node_for_q_bit(me[1], equivalence)
        temp = (q1, q2, me[2])
        h_edges_given.append(temp)
    return h_edges_given


def find_which_edges_are_violating_adjacency(h_edges_given: list, h_adjacency_preset: dict):
    vio = []
    n_vio = []
    for he in h_edges_given:
        if he[1] in h_adjacency_preset[he[0]]:
            n_vio.append(he)
        else:
            vio.append(he)
    return n_vio, vio


def connect_these_vertices(vertices: list):
    path = []
    for i in range(0, len(vertices) - 1):
        temp = (vertices[i], vertices[i + 1], '')
        path.append(temp)
    return path


def get_all_shortest_paths_for_violated_edges(violated_edges: list, h_adjacency_preset: dict, h_vertices: list):
    locked_paths = {}
    i = 0
    locked_swaps = {}
    for ve in violated_edges:
        path, path_distance, no_of_swaps = ap.get_shortest_path_with_distance_and_corresponding_swapping(
            h_adjacency_preset, ve[0], ve[1], h_vertices
        )
        locked_paths[i] = connect_these_vertices(path)
        locked_swaps[i] = no_of_swaps
        i += 1
    return locked_paths, locked_swaps


def gather_all_edges_from_dictionary(locked_paths: dict):
    edges = []
    for k in locked_paths.keys():
        for lp in locked_paths[k]:
            edges.append(lp)
    return edges


def reverse_edge(edge: tuple):
    temp = (edge[1], edge[0], edge[2])
    return temp


def this_edge_in_list(edge: tuple, edge_list: list):
    """
        If given edge finds, then returns 69
        If reverse edge finds, then returns 96
        If edge doesn't find returns False.
    """
    for e in edge_list:
        re = reverse_edge(e)
        if e[0] == edge[0] and e[1] == edge[1]:
            return 69
        if re[0] == edge[0] and re[1] == edge[1]:
            return 96
    return False


def find_all_duplicates_of_this_edge(edge, edge_list: list):
    d = []
    r_edge = reverse_edge(edge)

    for e in edge_list:
        if e[0] == edge[0] and e[1] == edge[1]:
            d.append(e)
        if e[0] == r_edge[0] and e[1] == r_edge[1]:
            d.append(e)
    return d


def convert_in_one_edge(edges: list):
    weight = 0
    for e in edges:
        weight += convert_to_int(e[2])
    edge = [edges[0][0], edges[0][1], weight]
    return edge


def clear_up_duplicate_edges_by_maintaining_weights(edges: list):
    unique = []
    for e in edges:
        temp1 = find_all_duplicates_of_this_edge(e, edges)
        if len(temp1) != 1:
            temp2 = convert_in_one_edge(temp1)
            unique.append(temp2)
        else:
            unique.append(e)
    return unique


def convert_in_list_of_tuples(edges: list):
    final = []
    for e in edges:
        temp = (e[0], e[1], e[2])
        final.append(temp)
    return final


# noinspection PySimplifyBooleanCheck
def get_all_paths_for_merged_graph_with_final_weights(edges_not_violated: list, locked_paths: dict, locked_swaps: dict, edges_violated: list):
    # for i in range(0, len(edges_violated)):
    # for lp in locked_paths[i]:

    swap_paths = gather_all_edges_from_dictionary(locked_paths)

    weighted = []
    for sp in swap_paths:
        flag = this_edge_in_list(sp, edges_not_violated)
        if flag == False:
            temp = [sp[0], sp[1], 6]
            weighted.append(temp)
        else:
            if flag == 69:
                temp = [sp[0], sp[1], convert_to_int(sp[2]) + 6]
                weighted.append(temp)
            # if flag == 96:
            #     rsp = reverse_edge(sp)
            #     temp = [rsp[0], rsp[1], convert_to_int(rsp[2]) + 6]
            #     weighted.append(temp)

    for env in edges_not_violated:
        temp = [env[0], env[1], env[2]]
        weighted.append(temp)

    weighted = clear_up_duplicate_edges_by_maintaining_weights(weighted)
    weighted = convert_in_list_of_tuples(weighted)
    return weighted


def get_index_of(edge, edge_list: list):
    for i in range(0, len(edge_list)):
        if edge_list[i][0] == edge[0] and edge_list[i][1] == edge[1]:
            return i
    return None


# noinspection PySimplifyBooleanCheck
def replace_unweighted_edges_with_weights(h_edges: list, graph_edges: list):
    edges = []

    for e in h_edges:
        temp = [e[0], e[1], e[2]]
        edges.append(temp)

    for e in graph_edges:
        flag = this_edge_in_list(e, h_edges)
        if flag == 69:
            i = get_index_of(e, h_edges)
            edges[i][2] = e[2]
        if flag == 96:
            re = reverse_edge(e)
            i = get_index_of(re, h_edges)
            edges[i][2] = re[2]
        if flag == False:
            pass

    edges = convert_in_list_of_tuples(edges)
    return edges


def get_color_for_plotting_in_architecture(h_vertices: list, graph_nodes: list, h_edges: list, graph_edges: list):
    node_color_map = []
    edge_color_map = []

    for n in h_vertices:
        if n in graph_nodes:
            node_color_map.append('VIOLET')
        else:
            node_color_map.append('LIGHTGRAY')

    h_weighted_edges = replace_unweighted_edges_with_weights(h_edges, graph_edges)

    for e in h_weighted_edges:
        edge_color_map.append('LIGHTGRAY')

    return node_color_map, edge_color_map, h_weighted_edges


def get_total_cost_of_this_graph(h_weighted_edges: list):
    total = 0
    for hwe in h_weighted_edges:
        total += convert_to_int(hwe[2])
    return total


def get_total_cost_for_merged_graph(m_edges: list):
    total = 0
    for m in m_edges:
        total += convert_to_int(m[2])
    return total


def get_additional_cost(locked_swaps: dict):
    additional_cost = 3 * (com.calculate_total_violations(locked_swaps))
    return additional_cost


def get_costs(m_edges: list, locked_swaps: dict):
    additional_cost = get_additional_cost(locked_swaps)
    initial_cost = get_total_cost_for_merged_graph(m_edges)
    total_cost = additional_cost + initial_cost
    return initial_cost, additional_cost, total_cost

