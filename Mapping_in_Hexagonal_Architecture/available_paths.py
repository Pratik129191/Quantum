def BFS(hex_adjacency_list, source, destination, h_vertices, predecessor, distance):
    queue = []
    visited = {}
    for i in h_vertices:
        visited[i] = False
        distance[i] = 1000000
        predecessor[i] = -1

    visited[source] = True
    distance[source] = 0
    queue.append(source)

    while len(queue) != 0:
        u = queue[0]
        queue.pop(0)

        for i in hex_adjacency_list[u]:
            if not visited[i]:
                visited[i] = True
                distance[i] = distance[u] + 1
                predecessor[i] = u
                queue.append(i)

                if i == destination:
                    return True
    return False


def get_shortest_path_with_distance_and_corresponding_swapping(hex_adjacency_list, source, destination, h_vertices):
    predecessor = {}
    distance = {}
    for i in h_vertices:
        predecessor[i] = 0
        distance[i] = 0

    if not BFS(hex_adjacency_list, source, destination, h_vertices, predecessor, distance):
        print("Given source and destination are not connected")

    reversed_path = []
    crawl = destination
    reversed_path.append(crawl)

    while predecessor[crawl] != -1:
        reversed_path.append(predecessor[crawl])
        crawl = predecessor[crawl]

    path_distance = distance[destination]
    no_of_swaps = 2 * (path_distance - 1)
    path = []

    for i in range(len(reversed_path) - 1, -1, -1):
        path.append(reversed_path[i])

    return path, path_distance, no_of_swaps


def get_all_paths_utils(hex_adjacency_list, source, destination, visited, path, path_list):
    visited[source] = True
    path.append(source)

    if source == destination:
        path_list.append(path)
    else:
        for i in hex_adjacency_list[source]:
            if not visited[i]:
                get_all_paths_utils(hex_adjacency_list, i, destination, visited, path, path_list)

    path.pop()
    visited[source] = False


def get_all_paths(source, destination, h_vertices, hex_adjacency_list):
    visited = {}
    for h in h_vertices:
        visited[h] = False
    path = []
    path_list = []
    get_all_paths_utils(hex_adjacency_list, source, destination, visited, path, path_list)
    return path_list


