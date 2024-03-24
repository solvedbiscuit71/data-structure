t = 2

class Node:
    def __init__(self, key: list[int] | None = None, children: list['Node'] | None = None) -> None:
        self.key = [] if key is None else key
        self.children = [] if children is None else children

    def display(self):
        que: list[Node | None] = [self, None]
        while que:
            top = que.pop(0)
            if top is None:
                print('|')
                if que:
                    que.append(None)
                continue
            print('|', ' '.join(map(str, top.key)), end=' ')
            que.extend(top.children)

def insert(root: Node | None, key: int):
    """
    @assume key not in b-tree
    """
    if root is None:
        return Node([key])

    # balance the root node
    if len(root.key) == 2*t - 1:
        root = Node(
            [root.key[t-1]], 
            [Node(root.key[:t-1], root.children[:t]), Node(root.key[t:], root.children[t:])
        ])

    node = root
    while True:
        i = 0
        while i < len(node.key) and node.key[i] < key:
            i += 1

        if len(node.children) == 0:
            node.key.insert(i, key)
            break
        else:
            child = node.children[i]
            if len(child.key) == 2*t - 1:
                n1 = Node(child.key[:t-1], child.children[:t])
                n2 = Node(child.key[t:], child.children[t:])
                node.key.insert(i, child.key[t-1])
                node.children.pop(i)
                node.children.insert(i, n2)
                node.children.insert(i, n1)
            else:
                node = child
    return root
