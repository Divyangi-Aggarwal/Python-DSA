import networkx as nx
from Graph_visual import plot_graph

def add_edge_tograph(empty_matrix, number_vertex, first_node, second_node, graph_type):
    if first_node > number_vertex - 1 or second_node > number_vertex - 1:
        print(f"Invalid edge! Nodes must be between 0 and {number_vertex - 1}.")
    else:
        empty_matrix[first_node][second_node] = 1
        if graph_type.lower() != 'yes':  # undirected
            empty_matrix[second_node][first_node] = 1
    return empty_matrix

def lable_node(number_vertex):
    label_dict = {}
    for i in range(number_vertex):
        while True:
            label = input(f"Please enter the label for node {i}: ").strip()
            if label:
                label_dict[i] = label
                break
            else:
                print("Label cannot be empty. Try again.")
    return label_dict

def initialize_matrix(number_vertex):
    return [[0] * number_vertex for _ in range(number_vertex)]

def get_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ['yes', 'no']:
            return answer
        print("Please enter only 'yes' or 'no'.")

def get_integer(prompt, min_value=0, max_value=None):
    while True:
        try:
            value = int(input(prompt))
            if (max_value is None or value <= max_value) and value >= min_value:
                return value
            else:
                print(f"Please enter a number between {min_value} and {max_value if max_value is not None else '∞'}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def main():
    while get_yes_no("Do you want to create a new graph? (yes/no): ") == 'yes':
        number_vertex = get_integer("Please enter the number of vertices/nodes: ", min_value=1)
        empty_matrix = initialize_matrix(number_vertex)

        want_to_label = get_yes_no("Do you want to give names to nodes? (yes/no): ")
        label_dict = lable_node(number_vertex) if want_to_label == 'yes' else {i: str(i) for i in range(number_vertex)}

        graph_type = get_yes_no("Do you want to create a directed graph? (yes/no): ")
        graph_create_using = nx.DiGraph if graph_type == 'yes' else nx.Graph

        while get_yes_no("Do you want to add an edge? (yes/no): ") == 'yes':
            first_node = get_integer("Enter the first node index: ", 0, number_vertex - 1)
            second_node = get_integer("Enter the second node index: ", 0, number_vertex - 1)
            empty_matrix = add_edge_tograph(empty_matrix, number_vertex, first_node, second_node, graph_type)

        plot_graph(empty_matrix, graph_create_using, label_dict)

    print("Thank you! Exiting the program.")


if __name__ == '__main__':
    main()
