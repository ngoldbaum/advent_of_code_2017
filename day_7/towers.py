class Node:
    def __init__(self, name, weight, children):
        self.name = name
        self.weight = weight
        self.children = children
        self.total_weight = weight

    def __repr__(self):
        repr = '%s (%s)' % (self.name, self.weight)
        if self.children is not None:
            child_str = '; '.join(
                [getattr(c, 'name', c) for c in self.children])
            repr += ' -> ' + child_str
        return repr


with open('input', 'r') as f:
    text = f.readlines()

text = [t.strip().split() for t in text]

names = [t[0] for t in text]
weights = [int(t[1].lstrip('(').strip(')')) for t in text]
children = [list(map(lambda x: x.strip(', '), t[3:]))
            if len(t) > 2 else None for t in text]

nodes = [Node(n, w, c) for n, w, c in zip(names, weights, children)]

for node in nodes:
    if node.children is not None:
        for i, child in enumerate(node.children):
            child = [n for n in nodes if n.name == child][0]
            node.children[i] = nodes[nodes.index(child)]

for node in nodes:
    if node.children is None:
        break

parent = node

while True:
    old_parent = parent
    for node in nodes:
        if node.children is not None and parent in node.children:
            parent = node
            break
    if old_parent == parent:
        break

root = parent


def process_child_weights(node):
    if node.children is None:
        return
    for child in node.children:
        process_child_weights(child)
        node.total_weight += child.total_weight


process_child_weights(root)


def balance(node):
    weights = [node.total_weight for node in node.children]
    for i, w in enumerate(weights):
        if weights.count(w) == 1:
            if balance(node.children[i]):
                print([c.weight for c in node.children])
                print([c.total_weight for c in node.children])
    if len(set(weights)) == 1:
        return True


balance(root)
