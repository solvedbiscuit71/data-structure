class Queue:
    def __init__(self, size=20):
        self.data = [None for _ in range(size)]
        self._front = 0
        self._back = 0
        self._size = size

    def __len__(self):
        return self._back - self._front

    def __str__(self) -> str:
        s = ', '.join(( str(self.data[(self._front + i) % self._size]) for i in range(self.__len__()) ))
        return '[' + s + ']' if s else '[]'

    def __repr__(self) -> str:
        return str(self)

    def enqueue(self, value):
        if self.__len__() == self._size:
            raise ValueError
        self.data[self._back % self._size] = value
        self._back += 1

    def dequeue(self):
        if self.__len__() == 0:
            raise ValueError
        front = self.data[self._front % self._size]
        self._front += 1
        return front

    def front(self):
        if self.__len__() == 0:
            raise ValueError
        return self.data[self._front % self._size]

    def back(self):
        if self.__len__() == 0:
            raise ValueError
        return self.data[(self._back - 1) % self._size]

if __name__ == "__main__":
    que = Queue(5)
    try:
        for x in range(10):
            que.enqueue(x)
    except ValueError:
        print('size exceed capacity')
    while que:
        value = que.dequeue()
        print(que, 'value popped:', value)

