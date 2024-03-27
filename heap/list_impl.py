class MinHeap:
    def __init__(self) -> None:
        self.tree = []

    def child(self, i):
        l = 2*i + 1 if 2*i + 1 < len(self.tree) else None
        r = 2*i + 2 if 2*i + 2 < len(self.tree) else None
        return l, r

    def min_child(self, i):
        l, r = self.child(i)
        if l and r:
            return r if self.tree[r] < self.tree[l] else l
        return l

    def parent(self, i):
        return (i-1) // 2 if i > 0 else None

    def bubble_up(self, i):
        j = self.parent(i)
        while j is not None:
            if self.tree[j] > self.tree[i]:
                self.tree[i], self.tree[j] = self.tree[j], self.tree[i]
                i = j
                j = self.parent(i)
            else:
                break

    def bubble_down(self, i):
        j = self.min_child(i)
        while j is not None:
            if self.tree[i] > self.tree[j]:
                self.tree[i], self.tree[j] = self.tree[j], self.tree[i]
                i = j
                j = self.min_child(i)
            else:
                break

    def push(self, value):
        self.tree.append(value)
        self.bubble_up(len(self.tree) - 1)

    def pop(self, value=None):
        if not self.tree:
            return None

        index = self.tree.index(value) if value is not None else 0
        self.tree[index], self.tree[-1] = self.tree[-1], self.tree[index]
        top = self.tree.pop()
        self.bubble_down(index)
        return top

    def top(self):
        return self.tree[0] if self.tree else None

    def __len__(self):
        return len(self.tree)

    def __str__(self):
        return str(self.tree)


if __name__ == "__main__":
    import random

    h = MinHeap()

    print("Adding...")
    for _ in range(5):
        x = random.randint(0, 20)
        print(x)
        h.push(x)

    print("Removing...")
    while h:
        print("front:", h.front())
        h.pop()


