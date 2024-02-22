from dataclasses import dataclass
from typing import Any

@dataclass
class Node:
    data: Any
    left: 'Node | None' = None
    right: 'Node | None' = None

class BT:
    def __init__(self, root = None) -> None:
        self.root: 'Node | None' = Node(root) if root else None

    @classmethod
    def from_preorder(cls, preorder: list, inorder: list):
        i = 0
        def construct(inorder: list):
            nonlocal i

            if not inorder:
                return None

            root = Node(preorder[i])
            i += 1
            if len(inorder) == 1:
                return root

            j = inorder.index(root.data)
            root.left = construct(inorder[:j])
            root.right = construct(inorder[j+1:])
            return root

        return construct(inorder)
