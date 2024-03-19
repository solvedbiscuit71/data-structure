from dataclasses import dataclass
from typing import Any

@dataclass
class Node:
    value: Any
    left: 'Node | None' = None
    right: 'Node | None' = None
    height = 0
    factor = 0

    def update(self):
        left_height = self.left.height if self.left else -1
        right_height = self.right.height if self.right else -1
        self.height = 1 + max(left_height, right_height)
        self.factor = right_height - left_height

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

def balance(node: Node) -> Node:
    if node.factor == -2 and node.left is not None:
        if node.left.factor == -1:
            return rotate_right(node)
        else:
            node.left = rotate_left(node.left)
            node.update()
            return balance(node)
    elif node.factor == 2 and node.right is not None:
        if node.right.factor == -1:
            node.right = rotate_right(node.right)
            node.update()
            return balance(node)
        else:
            return rotate_left(node)
    else:
        return node

def insert(node: Node | None, value: Any) -> Node:
    if node is None:
        return Node(value)
    elif node.value < value:
        node.right = insert(node.right, value)
    else:
        node.left = insert(node.left, value)
    node.update()
    return balance(node)

def contains(node: Node | None, value: Any) -> bool:
    if node is None:
        return False
    elif node.value == value:
        return True
    elif node.value < value:
        return contains(node.right, value)
    else:
        return contains(node.left, value)

def remove(node: Node | None, value: Any) -> Node | None:
    if node is None:
        return None
    elif node.value == value:
        # found the node!
        if node.left is None and node.right is None:
            return None
        elif node.left is not None and node.right is not None:
            # find the rightmost node in the left subtree
            tmp = node.left
            while tmp.right is not None:
                tmp = tmp.right
            # replace the value of rightmost node with value
            node.value = tmp.value
            tmp.value = value
            # delete the rightmost node in left subtree
            node.left = remove(node.left, value)
        elif node.left is not None:
            return node.left
        else:
            return node.right
    elif node.value < value:
        node.right = remove(node.right, value)
    else:
        node.left = remove(node.left, value)
    node.update()
    return balance(node)

def _inorder(node: Node | None):
    if node:
        _inorder(node.left)
        print(node.value, end=' ')
        _inorder(node.right)

def inorder(root):
    print("inorder: ", end='')
    _inorder(root)
    print()

if __name__ == "__main__":
    root = None
    print("inserting 5,3,8,1")
    root = insert(root, 5)
    root = insert(root, 3)
    root = insert(root, 8)
    root = insert(root, 1)
    inorder(root)

    print("is 3 in AVL?", contains(root, 3))
    print("removing 3")
    root = remove(root, 3)
    print("is 3 in AVL?", contains(root, 3))
    inorder(root)
