# Author: Zoljargal Gantumur
# Runtime: 212 ms
# Memory Usage: 17.9 MB

# Design a HashSet without using any built-in hash table libraries.
# To be specific, your design should include these functions:

# add(value): Insert a value into the HashSet. 
# contains(value) : Return whether the value exists in the HashSet or not.
# remove(value): Remove a value in the HashSet. 
# If the value does not exist in the HashSet, do nothing.

# Example:
# MyHashSet hashSet = new MyHashSet();
# hashSet.add(1);         
# hashSet.add(2);         
# hashSet.contains(1);    // returns true
# hashSet.contains(3);    // returns false (not found)
# hashSet.add(2);          
# hashSet.contains(2);    // returns true
# hashSet.remove(2);          
# hashSet.contains(2);    // returns false (already removed)

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyHashSet:

    def __init__(self):
        self.capacity = 8
        self.size = 0
        self.s = [None]*8
        self.lf = float(2)/3
        
    def myhash(self, key): 
        return key%self.capacity
        

    def add(self, key):
        if float(self.size)/self.capacity >= self.lf:
            self.capacity <<= 1
            ns = [None]*self.capacity
            for i in range(self.capacity >> 1):
                if self.s[i] and self.s[i] != "==TOMBSTONE==":
                    n = self.myhash(self.s[i])
                    while ns[n] is not None:
                        n = (5*n+1)%self.capacity
                    ns[n] = self.s[i]
            self.s = ns
        h = self.myhash(key)
        while self.s[h] is not None:
            if self.s[h] == key:
                return
            h = (5*h + 1) % self.capacity
            if self.s[h] == "==TOMBSTONE==":
                break
        self.s[h] = key
        self.size += 1
        
        

    def remove(self, key):
        h = self.myhash(key)
        while self.s[h]:
            if self.s[h] == key:
                self.s[h] = "==TOMBSTONE=="
                self.size -= 1
                return
            h = (5*h+1)%self.capacity
        

    def contains(self, key):
        h = self.myhash(key)
        while self.s[h] is not None:
            if self.s[h] == key:
                return True
            h = (5*h + 1)%self.capacity
        return False

        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
