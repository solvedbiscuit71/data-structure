class Queue:
    def __init__(self) -> None:
        self.data: list[int] = []

    def __len__(self) -> int:
        return len(self.data)

    def enque(self, elm):
        self.data.append(elm)

    def deque(self) -> int | None:
        return self.data.pop(0) if self.data else None

    def front(self) -> int | None:
        return self.data[0] if self.data else None

    def back(self) -> int | None:
        return self.data[-1] if self.data else None

if __name__ == "__main__":
    que = Queue()
    for elm in [1, 2, 3]:
        que.enque(elm)

    while que:
        print(que.front(), que.back())
        que.deque()
    print(que.front(), que.back())
