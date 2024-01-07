def dfs(graph: dict, start_node: tuple, end_nodes: list) -> bool:
    # depth first search algorithm
    visited = set()
    stack = [start_node]

    while stack:
        current_node = stack.pop()
        if current_node in end_nodes:
            return True
        visited.add(current_node)
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                stack.append(neighbor)
    return False


def check_path_red(graph: dict) -> bool:
    # creating set of end nodes
    end_nodes = []
    for x in range(135, 616, 120):
        end_nodes.append((x, 675))

    # checking path for every start node
    for x in range(135, 616, 120):
        start_node = (x, 75)
        if start_node not in graph:
            continue
        if dfs(graph, start_node, end_nodes):
            return True
    return False


def check_path_blue(graph: dict) -> bool:
    # creating set of end nodes
    end_nodes = []
    for y in range(135, 616, 120):
        end_nodes.append((675, y))

    # checking path for every start node
    for y in range(135, 616, 120):
        start_node = (75, y)
        if start_node not in graph:
            continue
        if dfs(graph, start_node, end_nodes):
            return True
    return False
