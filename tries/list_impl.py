from dataclasses import dataclass, field

@dataclass
class Node:
    is_complete: bool = False
    children: dict[str, 'Node'] = field(default_factory=dict)

    def __bool__(self):
        return self.is_complete

class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, s):
        if isinstance(s, str) and len(s) > 0:
            node = self.root
            for c in s:
                if node.children.get(c, None) is None:
                    node.children[c] = Node()
                node = node.children[c]
            node.is_complete = True
        else:
            raise TypeError

    def search(self, s, node=None):
        if isinstance(s, str) and len(s) > 0:
            node = self.root if node is None else node
            for c in s:
                node = node.children.get(c, None)
                if node is None:
                    break
            else:
                return (node.is_complete, node)
