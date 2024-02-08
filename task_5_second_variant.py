from collections import deque
import networkx as nx
import matplotlib.pyplot as plt
import uuid


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def dfs(tree_root):
    stack = [(tree_root, 0)]
    visited = set()

    while stack:
        node, depth = stack.pop()
        if node.val not in visited:
            visited.add(node.val)
            
            color = "#{:02X}{:02X}{:02X}".format(int("#d630f0"[1:3], 16), int("#d630f0"[3:5], 16),
                                                 int("#d630f0"[5:7], 16))
            node.color = color

            if node.right:
                stack.append((node.right, depth + 1))

            if node.left:
                stack.append((node.left, depth + 1))

            draw_tree(tree_root)  

    return visited


def bfs(tree_root):
    visited = []
    queue = deque([(tree_root, 0)])

    while queue:
        current_node, depth = queue.popleft()
        if current_node.val not in visited:
            visited.append(current_node.val)
            color = "#{:02X}{:02X}{:02X}".format(int("#1296F0"[1:3], 16), int("#1296F0"[3:5], 16),
                                                 int("#1296F0"[5:7], 16))
            current_node.color = color
            if current_node.left:
                queue.append((current_node.left, depth + 1))
            if current_node.right:
                queue.append((current_node.right, depth + 1))

            draw_tree(tree_root)

    return visited


root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

print(f"\nBFS: {bfs(root)}\n")
print(f"\nDFS: {dfs(root)}\n")
