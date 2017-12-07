class Node:
    def __init__(self, name, weight, children):
        self.name = name
        self.weight = weight
        self.children = children

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

child = node

while True:
    old_child = child
    for node in nodes:
        if node.children is not None and child in node.children:
            child = node
            break
    if old_child == child:
        break

print(child)
