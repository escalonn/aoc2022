import fileinput
import networkx as nx


def taxicab(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


G = nx.DiGraph()
data = G.nodes(data='height')

for i, line in enumerate(fileinput.input()):
    for j, char in enumerate(line.strip()):
        node = i, j
        if char == 'S':
            start = node
            char = 'a'
        elif char == 'E':
            end = node
            char = 'z'
        height = ord(char)
        G.add_node(node, height=height)
        for candidate in [(i - 1, j), (i, j - 1)]:
            if candidate in G:
                candidate_height = G.nodes[candidate]['height']
                if candidate_height <= height + 1:
                    G.add_edge(node, candidate)
                if height <= candidate_height + 1:
                    G.add_edge(candidate, node)

print(nx.astar_path_length(G, start, end, heuristic=taxicab))
