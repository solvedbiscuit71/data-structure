from enum import Enum, auto
from dataclasses import dataclass
from typing import Any

class Position(Enum):
    LEFT = auto()
    RIGHT = auto()

@dataclass
class Node:
    data: Any
    left: 'Node | None' = None
    right: 'Node | None' = None

    @staticmethod
    def addNode(parent: 'Node', position: Position, value: Any):
        match position:
            case Position.LEFT:
                if parent.left:
                    raise ValueError("Position already exists")
                parent.left = Node(value)
            case Position.RIGHT:
                if parent.right:
                    raise ValueError("Position already exists")
                parent.right = Node(value)

class BT:
    def __init__(self, root = None) -> None:
        self.root: 'Node | None' = Node(root) if root else None

    def insert(self, parent: Any, position: Position, value: Any):
        if not self.root:
            self.root = Node(value)
            return
        que = [self.root]
        while que:
            front = que.pop(0)
            if front.data == parent:
                Node.addNode(front, position, value)
                break
            if front.left:
                que.append(front.left)
            if front.right:
                que.append(front.right)
        else:
            raise ValueError("Parent not found")

    @staticmethod
    def _inorder(node: Node | None):
        if node:
            BT._inorder(node.left)
            print(node.data, end=' ')
            BT._inorder(node.right)

    def inorder(self):
        BT._inorder(self.root)
        print()

    @staticmethod
    def _preorder(node: Node | None):
        if node:
            print(node.data, end=' ')
            BT._preorder(node.left)
            BT._preorder(node.right)

    def preorder(self):
        BT._preorder(self.root)
        print()

if __name__ == "__main__":
    tree = BT(10)
    tree.insert(10, Position.LEFT, 20)
    tree.insert(10, Position.RIGHT, 30)
    tree.insert(30, Position.LEFT, 40)
    tree.insert(30, Position.RIGHT, 50)
    print("preorder:", end=' ')
    tree.preorder()
    print("inorder:", end=' ')
    tree.inorder()
