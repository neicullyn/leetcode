# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if head is None:
            return None
        
        d = dict()
        d[id(None)] = None
        
        new_head = RandomListNode(head.label)
        p = head
        q = new_head
        while p.next is not None:
            d[id(p)] = q
            q.next = RandomListNode(p.next.label)
            p = p.next
            q = q.next
        d[id(p)] = q
        p = head
        q = new_head
        while p is not None:
            q.random = d[id(p.random)]
            p = p.next
            q = q.next
        return new_head
        
a = RandomListNode(1)
b = RandomListNode(2)
c = RandomListNode(3)

a.next = b
b.next = c
a.random = c
b.random = None
c.random = a
print Solution().copyRandomList(a)
