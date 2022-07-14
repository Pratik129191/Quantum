def get_vertex_name_from(vertex: int):
    return str(str("H") + str(vertex))


def reverse_edge(edge: tuple):
    temp = (edge[1], edge[0], edge[2])
    return temp


def remove_duplicate_edges(edge_list: list):
    edges = []
    edges.extend(edge_list)

    for e in edges:
        re = reverse_edge(e)
        if e in edges and re in edges:
            edges.remove(e)
    return edges


def take_input_of_rows_and_columns():
    rows = int(input("Enter The Number of Rows in Architecture:\t"))
    cols = int(input("Enter The Number of Hexagons in Each Row:\t"))
    return rows, cols


def get_position(x: float, y: float):
    temp = [x, y]
    return temp


def arrange_borders(borders: list):
    arranged = [borders[0], borders[2], borders[3], borders[1], borders[5], borders[4]]
    return arranged


def get_vertex_in_this_position(pos: list, positions: dict):
    for key, value in positions.items():
        if value == pos:
            return str(key)
    return None


def get_vertices_positions_and_edges_for_one_hexagon(v, mid_x, mid_y, lower_x, lower_y, upper_x, upper_y, positions: dict):
    vert = []
    pos = {}
    borders = []
    edg = []
    center = ""

    # vertices & positions in the middle line ...
    for mid in range(0, 3):
        v_name = get_vertex_in_this_position(get_position(mid_x + mid, mid_y), positions)
        if v_name is not None:
            vert.append(v_name)
        else:
            v_name = get_vertex_name_from(v)
            v += 1
            vert.append(v_name)
            pos[v_name] = get_position(mid_x + mid, mid_y)

        if mid == 1:
            center = v_name
        else:
            borders.append(v_name)

    # vertices & positions in the lower line ...
    for low in range(0, 2):
        v_name = get_vertex_in_this_position(get_position(lower_x + low, lower_y), positions)
        if v_name is not None:
            vert.append(v_name)
        else:
            v_name = get_vertex_name_from(v)
            v += 1
            vert.append(v_name)
            pos[v_name] = get_position(lower_x + low, lower_y)
        borders.append(v_name)

    # vertices & positions in the upper line ...
    for up in range(0, 2):
        v_name = get_vertex_in_this_position(get_position(upper_x + up, upper_y), positions)
        if v_name is not None:
            vert.append(v_name)
        else:
            v_name = get_vertex_name_from(v)
            v += 1
            vert.append(v_name)
            pos[v_name] = get_position(upper_x + up, upper_y)
        borders.append(v_name)
    borders = arrange_borders(borders)

    # getting all edge connection ...
    for i in range(0, len(borders)-1):
        temp = [
            (borders[i], borders[i+1], ''),
            (borders[i+1], borders[i], '')
        ]
        for t in temp:
            edg.append(t)
    temp = [
        (borders[0], borders[-1], ''),
        (borders[-1], borders[0], '')
    ]
    for t in temp:
        edg.append(t)
    for b in borders:
        temp = [
            (center, b, ''),
            (b, center, '')
        ]
        for t in temp:
            edg.append(t)

    return v, vert, pos, edg


def copy_vertices(temp_vertices: list, vertices: list):
    for v in temp_vertices:
        if v not in vertices:
            vertices.append(v)
    return vertices


def copy_positions(temp_positions: dict, positions: dict):
    for p in temp_positions:
        if p not in positions:
            positions[p] = temp_positions[p]
    return positions


def copy_edges(temp_edges: list, edges: list):
    for e in temp_edges:
        if e not in edges:
            edges.append(e)
    return edges


def gather_information_about_all_hexagons(rows: int, columns: int):
    start_x, start_y = 1, 2
    vertices = []
    edges = []
    positions = {}
    v = 1
    for r in range(0, (2*rows), 2):
        for c in range(0, columns):
            mid_x, mid_y = start_x + c, start_y + r
            lower_x, lower_y = mid_x + 0.5, mid_y - 1
            upper_x, upper_y = mid_x + 0.5, mid_y + 1

            v, temp_vertices, temp_positions, temp_edges = get_vertices_positions_and_edges_for_one_hexagon(
                v, mid_x, mid_y, lower_x, lower_y, upper_x, upper_y, positions
            )

            vertices = copy_vertices(temp_vertices, vertices)
            positions = copy_positions(temp_positions, positions)
            edges = copy_edges(temp_edges, edges)
    edges = remove_duplicate_edges(edges)
    # print(edges)
    return vertices, positions, edges


def figure_up_the_hexagonal_architecture():
    rows, cols = take_input_of_rows_and_columns()
    vertices, positions, edges = gather_information_about_all_hexagons(rows, cols)
    return vertices, positions, edges
