import random
import architecture as arch


def x_in_str(x, string: str):
    for i in range(0, len(string)):
        if string[i] == x:
            return True
    return False


def get_corresponding_h_node_for_q_bit(qbit, equivalence: list):
    for e in equivalence:
        if qbit == e[1]:
            return e[0]


def is_any_reverse_edge(edges: list):
    for x in edges:
        count = 0
        for e in edges:
            if x[0] == e[0] and x[1] == e[1]:
                count += 1
            if x[1] == e[0] and x[0] == e[1]:
                count += 1

            if count > 1:
                return True
            else:
                return False


def initialize_vertex_points_for_merged_graph(m_vertices: list, h_vertices: list):
    points = []

    while len(points) != len(m_vertices):
        index = random.randint(1, len(h_vertices))
        if index not in points:
            points.append(index)
    return points


def create_vertex_names_from_random_points(points: list):
    vertices = []
    for p in points:
        h = arch.get_vertex_name_from(p)
        vertices.append(h)
    return vertices


def get_equivalence_points_for_plotting_graph(m_vertices: list, h_nodes: list):
    equivalence = []
    for i in range(0, len(h_nodes)):
        temp = (h_nodes[i], m_vertices[i])
        equivalence.append(temp)
    return equivalence


def calculate_total_violations(violations: dict):
    total = 0
    for v in violations:
        total += violations[v]
    return total


def get_all_violations_for_every_plotting(essentials: dict):
    violations = {}

    for e in essentials:
        violations[e] = essentials[e][3]
    return violations


def find_minimum_violations_and_corresponding_plotting(all_violations: dict, essentials: dict):
    keys = list(all_violations.keys())
    lowest = all_violations[keys[0]]
    minimum_violations = {}

    for k in keys:
        if all_violations[k] < lowest:
            lowest = all_violations[k]

    for av in all_violations:
        if all_violations[av] == lowest:
            minimum_violations[av] = essentials[av]
    return minimum_violations, lowest


def get_desired_element_from_list(choice: int, input_list: list):
    k = choice - 1
    return input_list[k]


def unpack_information_for_particular_plotting(choice: int, plot_book: dict):
    key = get_desired_element_from_list(choice, list(plot_book.keys()))
    infos = plot_book[key]
    h_weighted_edges = infos[0]
    node_color_map = infos[1]
    edge_color_map = infos[2]
    total_violations = infos[3]
    equivalence_mapping = infos[4]
    total_cost = infos[5]
    additional_cost = infos[6]
    initial_cost = infos[7]

    return h_weighted_edges, node_color_map, edge_color_map, total_violations, equivalence_mapping, total_cost, additional_cost, initial_cost


def unpack_information_for_this_plotting(plotting_packet: list):
    h_weighted_edges = plotting_packet[0]
    node_color_map = plotting_packet[1]
    edge_color_map = plotting_packet[2]
    total_violations = plotting_packet[3]
    equivalence_mapping = plotting_packet[4]
    total_cost = plotting_packet[5]
    additional_cost = plotting_packet[6]
    initial_cost = plotting_packet[7]

    return h_weighted_edges, node_color_map, edge_color_map, total_violations, equivalence_mapping, total_cost, additional_cost, initial_cost


