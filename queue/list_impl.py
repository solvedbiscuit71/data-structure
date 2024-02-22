from dataclasses import dataclass

@dataclass
class Node:
    data: int
    next: 'Node | None' = None

class Queue:
    def __init__(self) -> None:
        self.head: 'Node | None' = None
        self.tail: 'Node | None' = None

    def __bool__(self) -> bool:
        return bool(self.head)

    def __str__(self) -> str:
        s = ''
        head = self.head
        while head:
            s += str(head.data) + ' -> '
            head = head.next
        s += str(None)
        return s

    def enque(self, element):
        if self.head:
            self.head = Node(element, self.head)
        else:
            self.tail = self.head = Node(element)

    def deque(self):
        if not self.head:
            return None

        if not self.head.next:
            popped = self.head
            self.head = self.tail = None
            return popped.data

        tail = self.head
        while tail.next and tail.next.next:
            tail = tail.next
        popped = tail.next
        tail.next = None
        self.tail = tail
        return popped.data # type: ignore

    def front(self):
        return self.tail.data if self.tail else None

    def back(self):
        return self.head.data if self.head else None


if __name__ == "__main__":
    que = Queue()
    for elm in [1, 2, 3]:
        que.enque(elm)

    while que:
        print(que.front(), que.back())
        que.deque()
    print(que.front(), que.back())
