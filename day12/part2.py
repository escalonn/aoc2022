import fileinput
import networkx as nx

starts = []
G = nx.DiGraph()
data = G.nodes(data='height')

for i, line in enumerate(fileinput.input()):
    for j, char in enumerate(line.strip()):
        node = i, j
        if char == 'S':
            char = 'a'
        elif char == 'E':
            end = node
            char = 'z'
        if char == 'a':
            starts.append(node)
        height = ord(char)
        G.add_node(node, height=height)
        for candidate in [(i - 1, j), (i, j - 1)]:
            if candidate in G:
                candidate_height = G.nodes[candidate]['height']
                if candidate_height <= height + 1:
                    G.add_edge(node, candidate)
                if height <= candidate_height + 1:
                    G.add_edge(candidate, node)

print(min(l for n, l in nx.single_target_shortest_path_length(G, end) if n in starts))
