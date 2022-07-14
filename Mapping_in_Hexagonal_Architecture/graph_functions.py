def get_graph_name(index):
    return str(str("G") + str(index))


def get_qbit_name(index):
    return str(str("Q") + str(index))


def get_ancilla_name(index):
    return str(str("A") + str(index))


def get_number_of_graphs_and_assign_names():
    no_of_graphs = int(input("Enter The Number Of Circuits (G):\t"))
    graphs = []
    for i in range(0, no_of_graphs):
        graphs.append(get_graph_name(i+1))
    return graphs


def get_number_of_qbit_names_and_target_name(graphs: list):
    qbit_names = []
    target_names = []
    for g in graphs:
        no_of_qbits = int(input(f"Enter The Number of Qbits for Graph {g}:\t"))
        temp = []
        for i in range(0, no_of_qbits):
            temp.append(get_qbit_name(i+1))

        target = input(f"Enter The Target Name for {g}:\t").upper()
        if target in temp:
            temp.remove(target)
        else:
            temp.remove(temp[-1])

        qbit_names.append(temp)
        target_names.append(target)

    return qbit_names, target_names


def ancilla_bits_are_possible(qbits: list):
    if len(qbits) - 2 > 0:
        return True
    return False


def get_all_ancilla_bits_per_graph(graphs: list, qbit_names: list):
    ancilla_names = []
    for g in range(0, len(graphs)):
        if ancilla_bits_are_possible(qbit_names[g]):
            no_of_ancilla = len(qbit_names[g]) - 2
            temp = []
            for i in range(0, no_of_ancilla):
                temp.append(get_ancilla_name(i+1))
            ancilla_names.append(temp)
        else:
            ancilla_names.append(None)
    return ancilla_names


def instantiate_all_edges_with_weights_for_every_graph(graphs: list, qbit_names: list, ancilla_names: list, target_names: list):
    locked_edges = []

    for g in range(0, len(graphs)):
        edges = []

        if ancilla_names[g] is not None:
            # append (a1 -- a2 -- a3 ... an)
            for anc in range(0, len(ancilla_names[g]) - 1):
                temp = (ancilla_names[g][anc], ancilla_names[g][anc + 1], 4)
                edges.append(temp)

            # append (a1--q2, a2--q3, ... an--qn+1)
            q = 1
            for anc in range(0, len(ancilla_names[g])):
                temp = (ancilla_names[g][anc], qbit_names[g][q], 4)
                edges.append(temp)
                q += 1

            # append remaining 4 edges
            temp = [
                (ancilla_names[g][-1], target_names[g], 2),
                (target_names[g], qbit_names[g][-1], 2),
                (qbit_names[g][-1], ancilla_names[g][-1], 2),
                (qbit_names[g][0], ancilla_names[g][0], 4)
            ]
            for t in temp:
                edges.append(t)

            locked_edges.append(edges)
        else:
            temp = [
                (qbit_names[g][0], qbit_names[g][1], '2'),
                (qbit_names[g][0], target_names[g], '2'),
                (qbit_names[g][1], target_names[g], 2)
            ]
            for t in temp:
                edges.append(t)

            locked_edges.append(edges)

    return locked_edges


def instantiate_all_vertices_for_every_graph(graphs: list, qbit_names: list, ancilla_names: list, target_names: list):
    locked_vertices = []
    for g in range(0, len(graphs)):
        vertices = []

        if ancilla_names[g] is not None:
            for q in qbit_names[g]:
                vertices.append(q)

            for a in ancilla_names[g]:
                vertices.append(a)

            vertices.append(target_names[g])

            locked_vertices.append(vertices)
        else:
            for q in qbit_names[g]:
                vertices.append(q)
            vertices.append(target_names[g])

            locked_vertices.append(vertices)

    return locked_vertices


# noinspection PyDictCreation
def instantiate_positions_and_colors_for_all_vertices_in_every_graph(graphs: list, qbit_names: list, ancilla_names: list, target_names: list, locked_vertices: list):
    positions = []
    node_color_maps = []
    for g in range(0, len(graphs)):
        if ancilla_names[g] is not None:
            pos = {}
            pos[target_names[g]] = [1, 1]
            pos[qbit_names[g][-1]] = [4, 1]

            x, y = 1, 3
            for i in range(len(ancilla_names[g]) - 1, -1, -1):
                pos[ancilla_names[g][i]] = [x, y]
                pos[qbit_names[g][i + 1]] = [x + 3, y]
                y += 2
            pos[qbit_names[g][0]] = [x, y]
            positions.append(pos)
        else:
            pos = {}
            pos[target_names[g]] = [1, 1]
            pos[qbit_names[g][-1]] = [4, 1]
            pos[qbit_names[g][0]] = [1, 3]
            positions.append(pos)

    for g in range(0, len(graphs)):
        if ancilla_names[g] is not None:
            color = []
            for lv in locked_vertices[g]:
                if lv in ancilla_names[g]:
                    color.append('PINK')
                if lv in qbit_names[g]:
                    color.append('VIOLET')
                if lv in target_names:
                    color.append('RED')
            node_color_maps.append(color)
        else:
            color = []
            for lv in locked_vertices[g]:
                if lv in qbit_names[g]:
                    color.append('VIOLET')
                if lv in target_names:
                    color.append('RED')
            node_color_maps.append(color)

    return positions, node_color_maps


def gather_all_information_for_all_graphs():
    graphs = get_number_of_graphs_and_assign_names()
    qbit_names, target_names = get_number_of_qbit_names_and_target_name(graphs)
    ancilla_names = get_all_ancilla_bits_per_graph(graphs, qbit_names)
    locked_edges = instantiate_all_edges_with_weights_for_every_graph(graphs, qbit_names, ancilla_names, target_names)
    locked_vertices = instantiate_all_vertices_for_every_graph(graphs, qbit_names, ancilla_names, target_names)
    positions, node_color_maps = instantiate_positions_and_colors_for_all_vertices_in_every_graph(graphs, qbit_names, ancilla_names, target_names, locked_vertices)
    return graphs, locked_edges, locked_vertices, positions, node_color_maps




