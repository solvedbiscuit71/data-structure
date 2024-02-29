class Node:
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left: 'Node | None' = left
        self.right: 'Node | None' = right
        self.update()

    # AVL properties
    def update(self):
        hl = self.left.h if self.left else -1
        hr = self.right.h if self.right else -1
        self.h = 1 + max(hl, hr)
        self.bf = hr - hl

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return str((self.left, self.value, self.right))

def rotate_right(node: Node):
    left: Node = node.left # type: ignore
    node.left = left.right
    left.right = node

    node.update()
    left.update()
    return left

def rotate_left(node: Node):
    right: Node = node.right # type: ignore
    node.right = right.left
    right.left = node

    node.update()
    right.update()
    return right

def update(node: Node | None):
    if node:
        update(node.left)
        update(node.right)
        node.update()
        print(node.value, node.h, node.bf)

if __name__ == '__main__':
    x = Node('A')
    x.left = Node('B')
    x.right = Node('C')
    x.left.left = Node('D')
    x.left.right = Node('E')
    x.right.left = Node('F')
    x.right.right = Node('G')

    print(x)
