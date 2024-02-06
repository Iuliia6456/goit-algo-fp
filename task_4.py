import heapq
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

def build_heap_tree(heap_array):
    if not heap_array:
        return None

    root = Node(heap_array[0])
    queue = [root]

    i = 1  # second element in the heap array
    while i < len(heap_array):
        current_node = queue.pop(0)

        left_child = Node(heap_array[i])
        current_node.left = left_child
        queue.append(left_child)
        i += 1

        if i < len(heap_array):
            right_child = Node(heap_array[i])
            current_node.right = right_child
            queue.append(right_child)
            i += 1

    return root


heap_array = [1, 3, 7, 9, 2, 4, 34, 1, 2]
heapq.heapify(heap_array)
print("\nHeapified array:", heap_array)

heap_tree_root = build_heap_tree(heap_array)

draw_tree(heap_tree_root)