import common
import graph_functions as gf
import merge_graphs as mg
import drawing as d
import architecture as arch
import manual_mapping as mm
import automated_mapping as am


graphs, locked_edges, locked_vertices, positions, node_color_maps = gf.gather_all_information_for_all_graphs()
d.draw_graphs(graphs, locked_edges, locked_vertices, positions, node_color_maps)

previous, new, m_vertices, m_edges, node_color_map = mg.merge_all_graphs(graphs, locked_edges, locked_vertices, positions, node_color_maps)
d.draw_merged_graph(previous, new, m_vertices, node_color_map)

h_vertices, h_positions, h_edges = arch.figure_up_the_hexagonal_architecture()
d.draw_hexagonal_architecture(h_vertices, h_positions, h_edges)

check = input("Do You Want to Perform Manual Mapping (Y/N):\t").upper()
# print(check)
# if check != str('N') or check != str('Y'):
#     print("Wrong Choice. | Mapping Terminated. | Please Try Again.")
#     exit(0)

if check == 'Y':
    h_weighted_edges, node_color_map, edge_color_map = mm.map_the_merged_graph_in_architecture_manually(
        h_vertices, h_edges, m_vertices, m_edges
    )
    d.draw_hexagonal_architecture_with_mapping(h_vertices, h_positions, h_weighted_edges, edge_color_map, node_color_map)
if check == 'N':
    max_loop = input("How Many Times You Want to Map [Stick to Default (100) by Pressing ENTER] :\t")
    if max_loop != '':
        max_loop = int(max_loop)
    else:
        max_loop = 100

    essentials, minimum_violations, lowest = am.perform_mapping_automatically(h_vertices, h_edges, m_vertices, m_edges, max_loop)

    print(f"There are {len(list(minimum_violations.keys()))} Plotting with Lowest Swaps {lowest}")

    decide = input(f"Do You Visualise {max_loop} Graphs Periodically (Y/N):\t").upper()
    if decide == 'N':
        min_decision = input("Do Yo Want to See All Graph with Minimum Violation Periodically (Y/N):\t").upper()
        if min_decision == 'Y':
            for e in minimum_violations:
                h_weighted_edges, node_color_map, edge_color_map, total_violations, equivalence_mapping, total_cost, additional_cost, initial_cost = \
                    common.unpack_information_for_this_plotting(minimum_violations[e])
                print(f"Total Number of Swaps for This Plotting is: {total_violations}")
                print(f"Total Cost For This Graph is {total_cost}")
                print(f"Initial Cost For This Graph was {initial_cost}")
                print(f"Additional Cost For This Graph is {additional_cost}")
                d.draw_hexagonal_architecture_with_mapping_for_automated_one(
                    h_vertices, h_positions, h_weighted_edges, edge_color_map, node_color_map, equivalence_mapping
                )
                input("Press Enter to Continue ...")
        if min_decision == 'N':
            choice = int(input(f"Enter Which One you Want to See (Between [1 --> {len(list(minimum_violations.keys()))}]) :\t"))
            if choice > len(list(minimum_violations.keys())):
                print("Maximum Length Exceeded. | System Terminated.")
            else:
                h_weighted_edges, node_color_map, edge_color_map, total_violations, equivalence_mapping, total_cost, additional_cost, initial_cost = \
                    common.unpack_information_for_particular_plotting(
                        choice, minimum_violations
                    )
                print(f"Total Number of Swaps for This Plotting is: {total_violations}")
                print(f"Total Cost For This Graph is {total_cost}")
                print(f"Initial Cost For This Graph was {initial_cost}")
                print(f"Additional Cost For This Graph is {additional_cost}")
                d.draw_hexagonal_architecture_with_mapping_for_automated_one(h_vertices, h_positions, h_weighted_edges, edge_color_map, node_color_map, equivalence_mapping)
    if decide == 'Y':
        for e in essentials:
            h_weighted_edges, node_color_map, edge_color_map, total_violations, equivalence_mapping, total_cost, additional_cost, initial_cost = \
                common.unpack_information_for_this_plotting(essentials[e])
            print(f"Total Number of Swaps for This Plotting is: {total_violations}")
            print(f"Total Cost For This Graph is {total_cost}")
            print(f"Initial Cost For This Graph was {initial_cost}")
            print(f"Additional Cost For This Graph is {additional_cost}")
            d.draw_hexagonal_architecture_with_mapping_for_automated_one(h_vertices, h_positions, h_weighted_edges, edge_color_map, node_color_map, equivalence_mapping)
            input("Press Enter to Continue ...")


def another_function():
    pass

