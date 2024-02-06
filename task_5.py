from collections import deque
import uuid
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
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
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def dfs(node, color='#e512f0'):
    visited = []
    stack = [(node, color)]

    while stack:
        current_node, current_color = stack.pop()
        if current_node.val not in visited:
            visited.append(current_node.val)
            current_node.color = current_color
            if current_node.right:
                stack.append((current_node.right, adjust_color(current_color)))
            if current_node.left:
                stack.append((current_node.left, adjust_color(current_color)))

    return visited


def bfs(tree_root, color='#f0cb12'):
    visited = []
    queue = deque([(tree_root, color)])

    while queue:
        current_node, current_color = queue.popleft()
        if current_node.val not in visited:
            visited.append(current_node.val)
            current_node.color = current_color
            if current_node.left:
                queue.append((current_node.left, adjust_color(current_color)))
            if current_node.right:
                queue.append((current_node.right, adjust_color(current_color)))

    return visited

def adjust_color(color):
    # Convert the color from hex to RGB
    r, g, b = int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16)

    # Darken the color 
    darken_factor = 0.7  
    r = max(0, int(r * darken_factor))
    g = max(0, int(g * darken_factor))
    b = max(0, int(b * darken_factor))

    # Convert the darkened RGB values back to hex
    darkened_color = "#{:02X}{:02X}{:02X}".format(r, g, b)

    return darkened_color


root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

dfs_colors = dfs(root)
draw_tree(root)

bfs_colors = bfs(root)
draw_tree(root)

print("\nDFS:", dfs_colors)
print("\nBFS:", bfs_colors)


