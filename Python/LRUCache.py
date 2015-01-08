import collections
class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.queue = collections.deque()
        self.hash_num = dict()
        self.hash_index = dict()
        self.capacity = capacity
        self.n = 0
        self.cache = [0 for _ in range(capacity)]
    
    def _update(self, key):
        if self.hash_num.has_key(key):
            self.hash_num[key] += 1
        else:
            self.hash_num[key] = 1
        self.queue.append(key)  
    
        

    # @return an integer
    def get(self, key):
        if self.hash_index.has_key(key):
            self._update(key)
            return self.cache[self.hash_index[key]]
        else:
            return -1
        

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if self.hash_index.has_key(key):
            self.cache[self.hash_index[key]] = value
            self._update(key)
                    
        else:
            if self.n == self.capacity:
                while True:
                    dkey = self.queue.popleft()
                    self.hash_num[dkey] -= 1
                    if self.hash_num[dkey] == 0:                    
                        index = self.hash_index[dkey]
                        del self.hash_num[dkey]
                        del self.hash_index[dkey]
                        break;
                self.cache[index] = value
                self.hash_index[key] = index
                self._update(key)
            else:
                index = self.n
                self.cache[index] = value
                self.hash_index[key] = index
                self._update(key)
                self.n += 1

        
c = LRUCache(3)
print c.get(1)
c.set(1,1)
print c.get(1)
c.set(2,2)
c.set(3,3)
c.set(1,1)
c.set(4,4)
for i in range(1,5):
    print i, c.get(i)

print '----'
c = LRUCache(2)
print c.get(2)
c.set(2,6)
print c.get(1)
c.set(1,5)
c.set(1,2)
print c.get(1)
print c.get(2)



        