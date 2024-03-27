class IndexedMinHeap:
    def __init__(self, maxindex) -> None:
        self.maxindex = maxindex  # index belongs to [0, maxindex]
        self.size = 0
        self.tree: list[int] = [None for _ in range(maxindex + 1)]  # heap stores index # type: ignore
        self.loc: list[int] = [None for _ in range(maxindex + 1)]  # location of a particular index in the heap # type: ignore
        self.key = [None for _ in range(maxindex + 1)]  # index-key table # type: ignore

    def child(self, i):
        l = 2*i + 1 if 2*i + 1 < self.size else None
        r = 2*i + 2 if 2*i + 2 < self.size else None
        return l, r

    def min_child(self, i):
        l, r = self.child(i)
        if l and r:
            return r if self.key[self.tree[r]] < self.key[self.tree[l]] else l
        return l

    def parent(self, i):
        return (i-1) // 2 if i > 0 else None

    def bubble_up(self, i):
        j = self.parent(i)
        while j is not None:
            if self.key[self.tree[j]] > self.key[self.tree[i]]:
                self.tree[i], self.tree[j] = self.tree[j], self.tree[i]
                self.loc[self.tree[i]], self.loc[self.tree[j]] = self.loc[self.tree[i]], self.loc[self.tree[j]]
                i = j
                j = self.parent(i)
            else:
                break

    def bubble_down(self, i):
        j = self.min_child(i)
        while j is not None:
            if self.key[self.tree[i]] > self.key[self.tree[j]]:
                self.tree[i], self.tree[j] = self.tree[j], self.tree[i]
                self.loc[self.tree[i]], self.loc[self.tree[j]] = self.loc[self.tree[i]], self.loc[self.tree[j]]
                i = j
                j = self.min_child(i)
            else:
                break

    def push(self, i, key):
        if not (0 <= i <= self.maxindex):
            raise Exception("Index exceeds maxindex")

        if self.loc[i] is not None:
            raise Exception("Index already exist")

        self.tree[self.size] = i
        self.loc[i] = self.size
        self.key[i] = key
        self.size += 1
        self.bubble_up(self.size - 1)

    def pop(self):
        if self.size == 0:
            return None

        i = self.tree[0]
        key = self.key[i]
        self.key[i] = None
        self.loc[i] = None # type: ignore

        self.tree[0] = self.tree[self.size - 1]
        self.loc[self.tree[self.size - 1]] = 0
        self.tree[self.size - 1] = None # type: ignore

        self.size -= 1
        if self.size > 0:
            self.bubble_down(0)
        return (i, key)

    def setKey(self, i, key):
        if self.key[i] is None:
            raise Exception("Index doesn't exist")

        old_key = self.key[i]
        self.key[i] = key
        if key > old_key:
            self.bubble_down(self.loc[i])
        elif key < old_key:
            self.bubble_up(self.loc[i])

    def getKey(self, i):
        if self.key[i] is None:
            raise Exception("Index doesn't exist")
        return self.key[i]

    def top(self):
        return (self.tree[0], self.key[self.tree[0]]) if self.tree else None

    def __len__(self):
        return self.size

    def __contains__(self, i):
        return self.loc[i] is not None

