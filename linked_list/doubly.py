from dataclasses import dataclass

@dataclass
class Node:
    data: int
    next: 'Node | None' = None
    prev: 'Node | None' = None

    def __repr__(self) -> str:
        return '({}, {}, {})'.format(
            self.prev.data if self.prev else None,
            self.data,
            self.next.data if self.next else None
        )

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head: 'Node | None' = None
        self.tail: 'Node | None' = None
        self.size: int = 0

    def __bool__(self) -> bool:
        return bool(self.head)

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

    def __repr__(self) -> str:
        return str(self)

    def __len__(self) -> int:
        return self.size

    def _get_node(self, index: int) -> 'Node | None':
        if index < 0:
            index += self.size

        i = 0
        if index < abs(index - self.size + 1):
            head = self.head
            while head and i < index:
                head = head.next
                i += 1
            return head
        else:
            tail = self.tail
            index = abs(index - self.size + 1)
            while tail and i < index:
                tail = tail.prev
                i += 1
            return tail

    def __getitem__(self, index: int) -> int:
        head = self._get_node(index)
        if head:
            return head.data
        else:
            raise IndexError

    def __setitem__(self, index: int, value: int):
        head = self._get_node(index)
        if head:
            head.data = value
        else:
            raise IndexError

    def append(self, element):
        if self.tail:
            self.tail.next = Node(element, prev=self.tail)
            self.tail = self.tail.next
        else:
            self.head = self.tail = Node(element)
        self.size += 1

    def pop(self, index=-1):
        head = self._get_node(index)
        if head:
            if head.next and head.prev:
                head.next.prev = head.prev
                head.prev.next = head.next
            elif head.next:
                head.next.prev = head.prev
                self.head = head.next
            elif head.prev:
                head.prev.next = head.next
                self.tail = head.prev
            else:
                self.head = self.tail = None
            head.next = head.prev = None
            self.size -= 1
            return head.data
        else:
            raise IndexError

    def insert(self, index, element):
        size = self.__len__()
        if index < 0:
            index += size

        head = self._get_node(index)
        if head:
            node = Node(element)
            if head.prev:
                node.prev = head.prev
                head.prev.next = node
            else:
                self.head = node
            node.next = head
            head.prev = node
            self.size += 1
        else:
            raise IndexError

    def remove(self, element):
        head = self.head
        while head:
            if head.data == element:
                break
            head = head.next
        
        if head:
            if head.next and head.prev:
                head.next.prev = head.prev
                head.prev.next = head.next
            elif head.next:
                head.next.prev = head.prev
                self.head = head.next
            elif head.prev:
                head.prev.next = head.next
                self.tail = head.prev
            else:
                self.head = self.tail = None
            head.next = head.prev = None
            self.size -= 1
            return head.data
        else:
            raise ValueError

if __name__ == "__main__":
    x = DoublyLinkedList()
    for i in range(5):
        x.append(i)
    print(x)
    print('Delete element at 2th position')
    x.pop(2)
    print(x)
    print('Add element at 1st position')
    x.insert(0, 10)
    print(x)
    print('Remove element whose value = 3')
    x.remove(3)
    print(x)
