from dataclasses import dataclass
from typing import Any

@dataclass
class Node:
    data: Any
    left: 'Node | None' = None
    right: 'Node | None' = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = insert(self.root, value)

    def remove(self, value):
        self.root = remove(self.root, value)

    def search(self, value):
        node = search(self.root, value)
        return node is not None

    def display(self):
        display(self.root)
        print()

    def __len__(self):
        count = 0
        def __inorder(node):
            nonlocal count
            if node:
                __inorder(node.left)
                count += 1
                __inorder(node.right)
        __inorder(self.root)
        return count

    def __iter__(self):
        it = []
        def __inorder(node):
            nonlocal it
            if node:
                __inorder(node.left)
                it.append(node.data)
                __inorder(node.right)
        __inorder(self.root)
        return iter(it)

def insert(node, value):
    if node:
        if node.data > value:
            node.left = insert(node.left, value)
        else:
            node.right = insert(node.right, value)
        return node
    return Node(value)


def remove(node, value):
    if node:
        if node.data > value:
            node.left = remove(node.left, value)
        elif node.data < value:
            node.right = remove(node.right, value)
        else:
            if not node.left:
                return node.right
            if not node.right:
                return node.left

            # inorder successor
            tmp = node.right
            while tmp.left:
                tmp = tmp.left
            node.data = tmp.data
            node.right = remove(node.right, tmp.data)

            return node
        return node


def search(node: 'Node | None', value):
    if node:
        if node.data < value:
            return search(node.right, value)
        if node.data > value:
            return search(node.left, value)
        return node


def display(node: 'Node | None'):
    if node:
        display(node.left)
        print(node.data, end=' ')
        display(node.right)

if __name__ == "__main__":
    import random

    values = list(range(10))
    random.shuffle(values)
    print("Inserting...", ' '.join(map(str, values)))

    t = BST()
    for value in values:
        t.insert(value)
    t.display()
    t.remove(7) # delete
    t.display()
    print("Is 7 in BST?", t.search(7))
