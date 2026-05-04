class MyHashMap:

    def __init__(self):
        self.items = [-1] * (10**6 + 1)
        

    def put(self, key: int, value: int) -> None:
        self.items[key] = value
        return
        

    def get(self, key: int) -> int:
        return self.items[key]
        

    def remove(self, key: int) -> None:
        self.items[key] = -1
        return
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

# time complexity: O(1) for all operations (put, get, remove) since we are using a direct access array to store the values based on the keys.
# space complexity: O(N) where N is the maximum key value (10^6 in this case) since we are using a list to store the values for all possible keys.