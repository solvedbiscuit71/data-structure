from dataclasses import dataclass

@dataclass
class Node:
    data: int
    next: 'Node | None' = None

class Stack:
    def __init__(self) -> None:
        self.head: 'Node | None' = None

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

    def push(self, element):
        self.head = Node(element, self.head)

    def pop(self):
        if self.head:
            popped = self.head
            self.head = popped.next
            popped.next = None
            return popped.data
        else:
            return None

    def top(self):
        return self.head.data if self.head else None

if __name__ == "__main__":
    stk = Stack()
    for elm in [1, 2, 3]:
        stk.push(elm)

    while stk:
        print(stk.pop())
    print(stk.pop())
