from collections import deque
import uuid
import networkx as nx
import matplotlib.pyplot as plt
from tabulate import tabulate


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1, node_colors=None):
    if node is not None:
        graph.add_node(node.id, color=node_colors[node.id], label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1, node_colors=node_colors)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1, node_colors=node_colors)
    return graph


def dfs(tree_root):
    stack = [(tree_root, False)]
    visited_order = 0
    node_colors = {}
    visited_nodes = []  

    while stack:
        node, visited = stack.pop()

        if node is not None:
            if not visited:

                color = "#{:02X}{:02X}{:02X}".format(40 * visited_order, 120, 200)
                node.color = color
                node_colors[node.id] = color
                visited_order += 1

                visited_nodes.append(node.val)  

                stack.append((node, True))  # visited
                stack.append((node.right, False))
                stack.append((node.left, False))

    return tree_root, node_colors, visited_nodes  


def bfs(tree_root):
    queue = deque([(tree_root, False)])
    visited_order = 0
    node_colors = {}
    visited_nodes = []

    while queue:
        node, visited = queue.popleft()

        if node is not None:
            if not visited:

                color = "#{:02X}{:02X}{:02X}".format(40 * visited_order, 200, 48)
                node.color = color
                node_colors[node.id] = color
                visited_order += 1

                visited_nodes.append(node.val)

                queue.append((node, True))  # visited
                queue.append((node.left, False))
                queue.append((node.right, False))

    return visited_nodes, node_colors

def draw_tree(tree_root, node_colors):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos, node_colors=node_colors)

    colors = [node_colors[node] for node in pos.keys()]
    labels = {node: tree.nodes[node]['label'] for node in tree.nodes()}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)


root, dfs_colors, visited_nodes = dfs(root)
draw_tree(root, dfs_colors)
print()
print("DFS table: visited nodes | colors")
table = tabulate((visited_nodes, dfs_colors.values()), tablefmt="fancy_grid", numalign="center")
print(table)
print()

visited_nodes_bfs, bfs_colors = bfs(root)
draw_tree(root, bfs_colors)
print()
print("BFS table: visited nodes | colors")
table_bfs = tabulate((visited_nodes_bfs, bfs_colors.values()), tablefmt="fancy_grid", numalign="center")
print(table_bfs)
print()



