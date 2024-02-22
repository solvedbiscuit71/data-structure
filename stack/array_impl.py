class Stack:
    def __init__(self) -> None:
        self.data: list[int] = []

    def __len__(self) -> int:
        return len(self.data)

    def push(self, elm):
        self.data.append(elm)

    def pop(self) -> int | None:
        return self.data.pop() if self.data else None

    def top(self) -> int | None:
        return self.data[-1] if self.data else None

if __name__ == "__main__":
    stk = Stack()
    for elm in [1, 2, 3]:
        stk.push(elm)

    while stk:
        print(stk.pop())
    print(stk.pop())
