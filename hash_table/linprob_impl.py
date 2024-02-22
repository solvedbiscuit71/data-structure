from dataclasses import dataclass
from typing import Any

@dataclass
class Slot:
    value: 'Any' = None
    deleted: bool = False

    def reset(self):
        self.value = None
        self.deleted = True

    def set(self, value):
        self.value = value
        self.deleted = False

    def __bool__(self):
        return self.value is not None

class HashTable:
    def __init__(self) -> None:
        self.table = [Slot() for _ in range(8)]
        self.count = 0

    def h(self, x):
        return hash(x) % len(self.table)

    def realloc(self):
        table = self.table
        self.table = [Slot() for _ in range(2*len(table))]
        self.count = 0
        for s in table:
            if s:
                self.insert(s.value)

    # Average Case: O(1) whereas Worst Case: O(n)
    def insert(self, x):
        if self.search(x):
            return

        # 0.75 is the load factor
        if self.count + 1 >= round(0.75 * len(self.table)):
            self.realloc()

        i = self.h(x)
        for _ in range(len(self.table)):
            # if empty slot (maybe deleted or not)
            if not self.table[i]:
                self.table[i].set(x)
                break
            i = (i+1)%len(self.table)
        self.count += 1

    def remove(self, x):
        i = self.h(x)
        for _ in range(len(self.table)):
            # if empty slot (not deleted)
            if not self.table[i] and not self.table[i].deleted:
                break

            # if correct slot
            elif self.table[i].value == x:
                self.table[i].reset()
                break

            i = (i+1)%len(self.table)

    def search(self, x):
        i = self.h(x)
        for _ in range(len(self.table)):
            # if empty slot (not deleted)
            if not self.table[i] and not self.table[i].deleted:
                break

            # if correct slot
            elif self.table[i].value == x:
                return True

            i = (i+1)%len(self.table)
        return False

    def __str__(self):
        x = map(lambda s: s.value if s.value is not None else None, self.table)
        return str(list(x))

    def __repr__(self) -> str:
        return self.__str__()

    def __len__(self):
        return self.count

if __name__ == "__main__":
    t = HashTable()
    values = [3.14, "hello", 47, (1, 2)]
    print("Inserting...", ' '.join(map(str, values)))
    for v in values:
        t.insert(v)

    print("[Table]:", t)

    print("Is 3.14 in Table?", t.search(3.14))
    print("Is (1, 2) in Table?", t.search((1, 2)))
    print("Removing... (1, 2)")
    t.remove((1, 2)) # remove
    print("[Table]:", t)
    print("Is (1, 2) in Table?", t.search((1, 2)))
