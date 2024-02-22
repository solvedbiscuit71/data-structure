from dataclasses import dataclass
from typing import Any

@dataclass
class Node:
    data: 'Any'
    next: 'Node | None' = None

class HashTable:
    def __init__(self) -> None:
        self.table: list[Node | None] = [None for _ in range(32)]

    def h(self, x):
        return hash(x) % len(self.table)

    def insert(self, x):
        if self.search(x):
            return

        i = self.h(x)
        head = self.table[i]
        if head is None:
            self.table[i] = Node(data=x)
        else:
            while head.next:
                head = head.next
            head.next = Node(data=x)

    def remove(self, x):
        i = self.h(x)
        head = self.table[i]
        prev = None
        while head and head.data != x:
            prev = head
            head = head.next
        if head is None:
            return
        elif prev is None:
            self.table[i] = head.next
        else:
            prev.next = head.next
    
    def search(self, x):
        i = self.h(x)
        head = self.table[i]
        while head and head.data != x:
            head = head.next
        return head is not None

if __name__ == "__main__":
    t = HashTable()
    values = [3.14, "hello", 47, (1, 2)]
    print("Inserting...", ' '.join(map(str, values)))
    for v in values:
        t.insert(v)

    print("Is 3.14 in Table?", t.search(3.14))
    print("Is (1, 2) in Table?", t.search((1, 2)))
    print("Removing... (1, 2)")
    t.remove((1, 2)) # remove
    print("Is (1, 2) in Table?", t.search((1, 2)))
