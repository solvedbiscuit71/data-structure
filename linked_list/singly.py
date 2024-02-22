from dataclasses import dataclass

@dataclass
class Node:
    data: int
    next: 'Node | None' = None

    def __repr__(self) -> str:
        return '({}, {})'.format(
            self.data,
            self.next if self.next else None
        )

class SinglyLinkedList:
    def __init__(self) -> None:
        self.head: 'Node | None' = None
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
        head = self.head
        while head and i < index:
            head = head.next
            i += 1
        return head

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
        head = self._get_node(-1)
        if head:
            head.next = Node(element)
        else:
            self.head = Node(element)
        self.size += 1

    def pop(self, index=-1):
        if (index == 0 or index == -self.size) and self.head:
            self.head = self.head.next
        else:
            prev = self._get_node(index - 1)
            head = prev.next if prev else None
            if head:
                if prev:
                    prev.next = head.next
                elif self.head == head:
                    self.head = self.head.next # type: ignore
                self.size -= 1
                return head.data
            else:
                raise IndexError

    def insert(self, index, element):
        if index == 0 or index == -self.size:
            self.head = Node(element, next=self.head)
            self.size += 1
        else:
            head = self._get_node(index - 1)
            if head:
                head.next = Node(element, next=head.next)
                self.size += 1
            else:
                raise IndexError

    def remove(self, element):
        prev = None
        head = self.head
        while head:
            if head.data == element:
                break
            prev = head
            head = head.next
        
        if head:
            if prev:
                prev.next = head.next
            elif self.head == head:
                self.head = self.head.next # type: ignore
            self.size -= 1
            return head.data
        else:
            raise ValueError

if __name__ == "__main__":
    x = SinglyLinkedList()
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
