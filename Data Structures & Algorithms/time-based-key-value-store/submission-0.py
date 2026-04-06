from collections import namedtuple

class TimeMap:
    # feels similar to LRU cache
    Entry = namedtuple("Entry", ["value", "timestamp"])

    def __init__(self):
        self.cache = {} # key: values, timestamp

    def set(self, key: str, value: str, timestamp: int) -> None:
        # stores key with value at given timestamp in O(1) time
        if key not in self.cache:
            self.cache[key] = []
        
        self.cache[key].append(self.Entry(value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        # return most recent value of key, O(log n)
        if key not in self.cache:
            return ""

        entries = self.cache[key]

        # binary search for largest timestamp <= given timestamp
        lo, hi = 0, len(entries) - 1
        result = ""

        while lo <= hi:
            mid = (lo + hi) // 2
            if entries[mid].timestamp <= timestamp:
                result = entries[mid].value
                lo = mid + 1
            else:
                hi = mid - 1
        
        return result

        