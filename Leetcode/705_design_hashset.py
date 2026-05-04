class MyHashSet:

    def __init__(self):
        self.items = []

    def add(self, key: int) -> None:
        if key not in self.items:
            self.items.append(key)

    def remove(self, key: int) -> None:
        if key in self.items:
            self.items.remove(key)

    def contains(self, key: int) -> bool:
        if key in self.items:
            return True
        else:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

# ----------------------------------------------------------------------
# Bucket Hashing

class MyHashSet:
    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def add(self, key: int) -> None:
        bucket = self.buckets[self._hash(key)]
        if key not in bucket:
            bucket.append(key)

    def remove(self, key: int) -> None:
        bucket = self.buckets[self._hash(key)]
        if key in bucket:
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.buckets[self._hash(key)]

# ---------------------------------------------------------------------
# New Approach

class MyHashSet:

    def __init__(self):
        self.items = [False] * (10**6 + 1)

    def add(self, key: int) -> None:
        self.items[key] = True

    def remove(self, key: int) -> None:
        self.items[key] = False

    def contains(self, key: int) -> bool:
        return self.items[key]

# time complexity: O(1) for add, remove, and contains operations since we are directly accessing the index in the list.
# space complexity: O(N) where N is the maximum key value (10^6 in this case) since we are using a list of boolean values to store the presence of keys in the hash set.