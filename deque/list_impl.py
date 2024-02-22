from dataclasses import dataclass
from typing import Any

@dataclass
class Node:
    data: 'Any'
    next: 'Node | None' = None

class Deque:
    def __init__(self) -> None:
        self.head: 'Node | None' = None

    def __len__(self) -> int:
        head = self.head
        size = 0
        while head:
            head = head.next
            size += 1
        return size

    def __str__(self) -> str:
        s = '['
        head = self.head
        while head:
            s += str(head.data) + ', '
            head = head.next
        if len(s) > 1:
            s = s[:-2]
        s += ']'
        return s

    def _tail(self) -> 'Node | None':
        tail = self.head
        if not tail:
            return tail
        while tail.next:
            tail = tail.next
        return tail

    def _before_tail(self) -> 'Node | None':
        tail = self.head
        if not tail:
            return tail
        while tail.next and tail.next.next:
            tail = tail.next
        return tail

    def addFirst(self, value):
        self.head = Node(value, self.head)

    def addLast(self, value):
        tail = self._tail()
        if tail:
            tail.next = Node(value)
        else:
            self.head = Node(value)

    def deleteFirst(self):
        if self.head:
            head = self.head
            self.head = self.head.next
            return head.data
        else:
            return None

    def deleteLast(self):
        node = self._before_tail()
        if node:
            if node.next:
                tail = node.next
                node.next = None
            else:
                tail = self.head
                self.head = None
            return tail.data # type: ignore
        else:
            return None
