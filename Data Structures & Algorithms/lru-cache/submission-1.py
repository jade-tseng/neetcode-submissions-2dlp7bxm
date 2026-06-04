class Node:
    def __init__(self, key=0, val=0):
        self.key, self.val = key, val
        self.prev = self.next = None
        
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _add_to_front(self, node): # head - Y - tail 
    # head - X - Y - tail
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        # once we get it, it moves to front of list (LRU):
        node = self.cache[key]
        self._remove(node)
        self._add_to_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache: # if key exists, update it: remove old node, then add new node
            self._remove(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node
        self._add_to_front(node)

        # If we're now over capacity, evict the least recently used node 
        # that's self.tail.prev. Remove it from both the linked list AND the hash map.
        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            # remove from cache too:
            del self.cache[lru.key]



        
