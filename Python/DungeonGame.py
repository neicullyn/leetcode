from sys import maxint

class Node:
    def __init__(self, pos, G, H, F):
        self.pos = pos
        self.G = G
        self.H = H
        self.F = F
        
    def __lt__(self, other):
        return self.F < other.F
    
    def __le__(self, other):
        return self.F <= other.F
    
    def __gt__(self, other):
        return self.F > other.F
    
    def __ge__(self, other):
        return self.F >= other.F
    
    def __str__(self):
        return 'pos=' + str(self.pos) + '  G=' + str(self.G) + '  H=' + str(self.H) + '  F=' + str(self.F) 
    
class PriorityQueue:
    def __init__(self, e0):
        self.lst = []
        self.lst.append(e0)
    
    def push(self, e):
        self.lst.append(e)
        self._percolate_up(len(self.lst)-1)
    
    def getTop(self):
        return self.lst[1]
    
    def pop(self):
        e = self.lst[1]
        self.lst[1], self.lst[-1] = self.lst[-1], self.lst[1]
        self.lst.pop()
        self._percolate_down(1)
        return e    
    
    def adjust(self, i):
        self._percolate_up(i)
        self._percolate_down(i)
    
    def _percolate_up(self, i):
        while True:
            if self.lst[i] < self.lst[i/2]:
                self.lst[i], self.lst[i/2] = self.lst[i/2], self.lst[i]
                i = i / 2
            else:
                break
                        
    def _percolate_down(self, j):
        while True:
            n = len(self.lst)
            if 2*j + 1 < n:
                # two child
                if self.lst[2*j] < self.lst[2*j+1]:
                    #left child is smaller
                    p = 2 * j
                else:
                    #right child is smaller
                    p = 2 * j + 1 
                if self.lst[j] > self.lst[p]:
                    #child is smaller than parent
                    self.lst[j], self.lst[p] = self.lst[p], self.lst[j]
                    j = p
                else:
                    break
            elif 2*j < n:
                # one child
                p = 2*j
                if self.lst[j] > self.lst[p]:
                    #child is smaller than parent
                    self.lst[j], self.lst[p] = self.lst[p], self.lst[j]
                    j = p
                else:
                    break
            else:
                # no child
                break
                
            
        
class Solution:
    # @param dungeon, a list of lists of integers
    # @return a integer
    
    def is_valid(self, pos):
        row = pos[0]
        col = pos[1]
        return 0 <= row and row < self.m and 0 <= col and col < self.n   
    
    def expand(self, pos):
        lst = []
#         for x in ((0,1), (0,-1), (1,0), (-1,0)):
        for x in ((0,1), (1,0)):
            new_pos = (pos[0]+x[0],pos[1]+x[1])
            if self.is_valid(new_pos):
                lst.append(new_pos)
        return lst
    
    def val(self, pos):
        return -self.dungeon[pos[0]][pos[1]] + self.base

    def calculateMinimumHP(self, dungeon):
        self.m = len(dungeon)
        self.n = len(dungeon[0])
        self.dungeon = dungeon
        self.base = max ([row[i] for row in dungeon for i in range(self.n)])
        open_list = dict()
        close_list = dict()
        heap = PriorityQueue(Node(pos=(-1, -1), G=0, H=0, F=-2147483648))
        
        pos = (0,0)
        node = Node(pos=pos, G=self.val(pos), H=1, F=self.val(pos))
        open_list[pos] = node
        heap.push(node)
        
        success = False
        while len(heap.lst)>1:
#             print node

            node = heap.pop()
#             print node
            if node.pos == (self.m-1, self.n-1):
                F = node.F
                H = node.H
                break
            if not open_list.has_key(node.pos):
                #not in open list, skip
                continue
            
            del open_list[node.pos]
            close_list[node.pos] = node          
            for x in self.expand(node.pos):
                if close_list.has_key(x):
                    # in close list
                    continue
                if node.G+self.val(x) > node.F:
                    new_node = Node(pos=x, G=node.G+self.val(x), H=x[0]+x[1], F=node.G+self.val(x))
                else:
                    new_node = Node(pos=x, G=node.G+self.val(x), H=node.H, F=node.F)
#                 new_node = Node(pos=x, G=node.G+self.val(x), H=0, F=max(node.G+self.val(x),node.F))
                if open_list.has_key(x):
                    # in open list         
                    old_node = open_list[x]           
                    if new_node < old_node:
                        # new_node is better
                        open_list[x] = new_node
                        heap.push(new_node)
                    else:
                        # old_node is better
                        # do nothing
                        pass
                else:
                    # not in open list
                    if node.G+self.val(x) > node.F:
                        new_node = Node(pos=x, G=node.G+self.val(x), H=x[0]+x[1], F=node.G+self.val(x))
                    else:
                        new_node = Node(pos=x, G=node.G+self.val(x), H=node.H, F=node.F)
#                     new_node = Node(pos=x, G=node.G+self.val(x), H=0, F=max(node.G+self.val(x),node.F))
                    open_list[x] = new_node
                    heap.push(new_node)
        F = F - H * self.base
        if F < 0:
            F = 0
        return F + 1
                
                     
            
        


        
        
s = Solution()
d=[[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
print s.calculateMinimumHP(d)

d=[[0]]
print s.calculateMinimumHP(d)
         
d=[[100]]
print s.calculateMinimumHP(d)

d=[[0,-74,-47,-20,-23,-39,-48],[37,-30,37,-65,-82,28,-27],[-76,-33,7,42,3,49,-93],[37,-41,35,-16,-96,-56,38],[-52,19,-37,14,-65,-42,9],[5,-26,-30,-65,11,5,16],[-60,9,36,-36,41,-47,-86],[-22,19,-5,-41,-8,-96,-95]]
print s.calculateMinimumHP(d)

d=[[-17,-89,-16,-29,-40,35,-31,-46,-53,-36,-25,47,-42,15,45,26,-62,36,-21,-53,-73,-17,-19,3,-86,-38,1,-55,-56,-29,-3,-68,-43,-58,-7,18,-86,-91,-7,37,-7,42,-67,-92,-88,-58,-59,-93,-74,-19,18,-40,28,0,-12,21,-96,-96,18,10,29,26,-1,-44,19,-11,-60,-6,-7,-40,15,-9,-34,26,-57,11,-42,-10,-29,-47,-92,-70,-35,31,-59,-28,-23,-23,-67,-2,-92,-71,-87,-80,-42,16,-75,-3,-79,39,-78,-94,-28,-91,21,-84,12,37,-18,-7,-83,11,-67,34,-67,-96,19,-47,-58,46,-93,12,-39,-66,-78,-64,14,39,-14,28],[-15,-98,12,-64,-50,4,39,-16,-71,14,43,15,13,-75,-25,41,-58,3,27,29,-71,-98,-84,-18,-64,44,-58,-27,-27,49,-15,43,17,-11,-66,-17,-96,18,-19,30,-26,-95,-96,-2,-37,-88,-66,-10,-41,41,-64,-34,-58,41,-14,40,-45,37,-53,-42,10,-69,-87,-99,45,-31,29,-29,16,19,-51,-4,-33,25,-41,-16,-50,33,-26,31,31,-78,-64,-81,19,45,-46,-96,-49,28,44,23,1,-45,-21,-33,-22,-59,-84,-54,-71,-13,-88,39,-22,-15,-23,1,16,-5,-55,24,-87,-42,-67,-18,-81,44,19,15,-80,-20,30,7,41,-61,-26,-96,9,42],[-22,-77,-69,17,43,-5,-79,16,16,-3,-74,50,1,0,6,-18,46,-95,39,45,-37,-4,-9,-45,-25,-34,6,-81,-51,-40,44,-38,35,-84,-1,-39,-45,-50,-30,-38,37,-37,23,-42,-64,-17,23,-15,-64,-2,-64,-20,-99,-48,22,-24,-98,-64,-66,38,-21,6,17,1,18,-18,-49,5,1,-6,-54,45,4,-1,14,-29,-39,-14,1,-47,-25,-60,-29,-76,-46,-42,-31,-96,-99,42,33,-67,-61,7,39,-34,-87,47,15,-8,-97,-71,-69,42,-29,4,13,-15,-59,48,-51,-67,35,-77,-51,19,-24,-54,-99,-47,-90,31,50,-50,48,8,-70,-84,-69,-99],[31,-85,34,-18,-64,-92,41,19,46,50,43,-74,-67,-89,15,45,-85,-55,-87,8,-24,-27,36,-77,-80,-50,48,-54,-100,-43,4,37,-76,0,-75,-85,-90,-54,0,-95,-64,10,-68,-11,-56,19,-8,16,7,-13,-24,-75,1,-18,-8,-96,-41,32,19,-36,-29,-63,-96,-52,27,40,-2,-45,-14,-43,-97,-57,-85,33,-86,-34,-62,-20,-58,26,11,-58,7,-50,-55,-51,-54,-51,-49,27,-18,35,-65,-86,45,22,-89,-81,-50,-17,-23,-73,-55,-51,-11,-96,24,-100,-28,-75,34,-14,-28,-23,26,34,-83,-65,45,42,-75,-25,13,30,-1,-57,43,-61,44,-23],[-22,29,19,-6,47,22,-49,-34,-58,-44,-20,14,-26,27,10,-88,-17,-46,-85,6,18,-18,-15,48,-45,-89,-24,-45,-19,-74,-72,-68,-3,-15,-51,-20,4,22,-31,26,-32,43,-17,38,-22,-6,-96,-71,-30,-14,28,38,12,26,8,-72,-19,-78,-47,-72,-79,38,-4,-15,-33,-68,29,-5,-64,35,-36,12,29,-73,2,-48,3,-95,-86,48,-28,20,-52,-82,8,49,1,-64,-3,-64,-58,-92,-97,-44,40,-94,-74,27,-10,3,-70,17,-98,-33,-26,-89,-15,-3,-11,-69,10,-53,-3,27,-49,-85,-92,-4,-25,-36,14,-25,-63,25,-73,-79,36,-7,-74,-78],[-89,-40,28,-98,47,24,44,-18,-80,33,-36,48,-90,-78,-84,-28,29,-45,-95,36,-92,-49,-3,-36,-53,40,4,-67,-81,18,-73,-68,35,-82,-79,18,-77,-22,-25,-97,28,-40,22,-21,-60,12,-54,-70,-29,-12,3,-24,-15,-79,-82,29,44,-85,-5,-64,-55,-25,40,48,-54,39,-80,-23,6,-7,28,-85,43,-40,-23,39,46,-78,-29,-68,-53,-19,-68,-72,29,13,-99,-46,-6,39,-86,-61,-77,-1,11,-82,23,34,33,-60,3,42,-50,13,26,-13,24,-47,-14,-56,15,-95,-88,-7,29,-97,29,-8,-8,-88,49,-19,3,-31,40,-35,15,-69,-75,-86],[-83,44,-29,-27,-100,21,-3,30,-24,24,10,-45,-5,-45,-15,-96,-99,-31,-16,-7,-83,-23,-69,-1,27,-94,3,-21,18,6,-99,-14,-18,-93,-20,-77,-55,26,47,-77,-91,-39,-99,50,39,-87,14,1,41,-3,-27,2,-47,31,-72,-33,3,21,-35,-47,-92,-19,-62,-53,-97,-33,26,-92,-1,-9,-14,-6,-22,-51,2,35,-65,-16,-83,33,-83,-66,9,0,18,36,23,-31,41,-60,-10,-95,-97,-28,-84,-81,-37,20,-52,-45,6,-55,-30,-99,3,28,-77,-23,-51,46,-98,-9,-20,-58,46,-80,17,39,-79,-95,-81,40,39,-1,-53,-91,-58,-62,-70,46],[43,-15,-1,-38,-36,-48,-98,-22,-53,-13,40,-28,-6,-72,-55,-68,-22,-77,-22,-64,-73,-68,27,-30,-88,47,-66,10,-73,-14,26,-39,37,-80,-69,-14,-9,-59,-29,-2,-62,-82,42,-62,10,-52,-64,-32,-49,-57,1,-35,9,46,-83,11,-72,3,25,37,-98,-24,2,-98,-2,-18,-3,-92,-96,-7,-78,-83,-40,-53,-60,-12,35,-29,4,-53,7,7,-2,-50,-58,-32,-24,-22,-12,-16,39,-42,29,-25,-55,-94,-79,-40,-68,24,14,-61,-97,-94,5,27,-25,30,-95,-58,-27,-99,-51,-61,-22,-65,-3,-43,-79,41,10,34,-60,-82,-92,-31,-69,-35,-91,16],[-12,8,-62,-12,-74,-84,-56,48,-66,-90,-46,-99,-63,8,-45,-55,-52,-88,2,39,15,37,31,16,-60,-100,-72,-46,-2,-44,-76,-40,-53,-48,10,-70,-22,42,-31,-93,-1,-24,-51,35,-44,42,-16,-73,-57,8,18,34,8,-77,-78,-17,-52,9,-62,47,11,34,-45,46,-22,13,-18,-48,22,-63,46,-12,-78,48,-97,-11,4,-37,-64,-25,-36,50,-16,-39,-67,45,-89,19,4,-23,21,23,-2,-19,-18,37,-14,-26,-90,-20,-75,-92,-43,-75,18,46,25,14,5,-55,-75,45,29,32,49,-80,-4,13,-35,-90,39,16,10,4,-95,-27,47,4,-4,-2],[43,-37,-21,-6,-94,-66,35,-19,18,-17,15,-51,14,-13,-51,-34,-35,-37,-35,-3,37,-38,-73,21,-76,-66,-70,-64,-21,-34,-14,-29,-66,6,11,-61,25,21,26,10,49,-69,-17,-42,-52,45,4,-2,-73,41,-65,47,-63,-95,-62,-32,-17,-60,-54,26,-79,21,-70,43,47,-61,37,-42,-61,-96,8,33,-88,-59,35,-39,-3,17,-93,-96,23,-57,-80,-21,-79,-6,-73,-60,-89,15,-47,-7,22,-29,-67,-51,-12,-21,12,8,-56,31,-87,-80,-32,9,14,2,-29,14,27,-35,-52,-27,40,9,-47,41,19,-19,-53,32,-78,26,12,-93,-39,-59,49,-43],[-48,18,20,-15,-89,41,31,-91,-11,-48,-67,-36,-87,6,-46,2,-37,-14,39,-95,19,-96,-37,12,-79,-56,-60,-99,-71,-97,20,-79,-69,-35,37,3,-59,27,-31,25,-93,42,-10,50,-87,-9,-95,40,30,-42,48,-49,-25,-66,-54,6,-57,7,-60,19,24,41,3,14,-72,-61,-73,-67,47,-1,-86,-77,9,3,-49,-33,-99,27,-95,-94,-41,2,27,-72,-5,-13,38,-53,16,-22,-54,16,-67,-38,-29,-85,-79,42,48,-71,43,-76,5,-98,-68,-25,18,49,35,-84,-55,48,-47,23,24,46,-88,-31,26,-76,19,-70,27,-47,45,-21,-92,-76,-75,27],[-34,25,-49,-49,-93,-84,-38,23,32,-57,-6,-24,-92,-36,-12,-8,46,-6,-46,-65,-32,2,35,39,-56,23,13,-42,-46,0,10,-13,26,46,-46,-37,29,44,-3,-85,-67,-98,14,-93,-52,-49,-9,-89,36,-75,9,6,-65,7,-22,9,43,36,-25,-31,-64,-48,-39,-100,-93,-47,-46,-47,-63,-62,-23,-79,-2,2,3,-21,-81,-64,-68,-67,-18,-59,26,-74,29,-73,36,20,-86,-34,3,2,-76,-5,18,-81,-25,23,-72,-67,22,-56,-24,21,-13,7,-97,-83,-53,-87,31,26,33,22,-33,-18,-68,48,-53,-64,-45,1,11,46,6,-70,21,18,-8,-49],[-96,29,28,-57,21,-86,12,0,-89,48,-17,-90,-88,-17,-30,-76,41,-9,-69,-10,-14,12,-51,21,-50,-100,-21,39,-97,-78,-85,-99,-42,11,-78,16,-88,-11,41,-87,32,18,-85,-49,20,29,43,4,14,-48,-15,-27,-96,-84,31,-46,18,-9,-87,-89,-10,27,-5,29,-47,-95,33,-43,24,-83,32,-98,-72,7,7,-72,-91,46,35,-70,-47,-67,-68,35,-4,-65,-3,-15,-38,-65,-59,-22,-9,-19,-14,-96,32,-26,22,-68,3,36,26,-36,-9,37,13,-28,6,-100,-76,30,25,-94,16,-21,38,-54,-41,-25,-26,-68,9,19,-45,-41,-96,49,-92,-87],[-78,31,3,-40,11,-25,-75,24,2,10,-7,24,-94,47,-69,-73,-22,-27,-30,27,-63,-28,-96,6,46,-22,17,21,-16,-22,9,37,-85,31,-53,-7,16,-8,-61,-21,49,44,-8,-71,-21,-69,-99,49,-90,18,2,-76,-43,37,-43,-30,38,-88,-18,36,-75,-87,-31,-38,-72,46,-46,-63,40,-34,-42,-3,-74,22,-15,4,24,14,-78,-14,-10,25,-86,16,40,-16,37,-56,-26,-28,-79,-6,-89,-42,-47,40,-82,-27,-60,-32,13,38,47,-10,19,1,-62,20,30,-32,-54,-88,-78,-4,-66,40,-93,-77,-72,-24,-40,19,-25,-60,2,-3,-57,-22,-52,-78],[4,41,13,5,42,-7,-30,-72,6,24,-87,27,32,-7,-82,-56,28,-22,48,-5,40,-43,39,42,-42,-50,-49,2,-51,17,-9,3,-99,21,-20,-93,-28,39,-24,-13,45,36,40,29,25,21,21,46,40,-70,-23,27,-20,-26,-46,37,-67,-82,39,-24,-25,-54,-92,-90,49,10,-25,-4,-35,-82,-30,-48,28,-17,-25,-44,42,4,-48,-59,-85,-56,-63,12,-49,50,18,-91,-26,26,-16,20,-59,49,30,-39,30,-41,-97,-49,-73,-94,-95,-100,-55,-60,-79,34,-42,-6,-66,-28,-78,-83,-78,-90,-63,-15,-50,-44,-74,-56,36,-90,-32,-100,-77,22,37,-21],[-24,-9,23,-29,-3,26,37,-74,-86,-74,-100,-89,-44,19,26,-8,-28,-39,-5,10,10,-70,-76,-72,32,-28,-31,29,-45,22,-29,-19,8,31,48,-11,-6,22,-75,-85,-54,-3,-38,-68,-27,-69,-81,-92,-18,-50,-12,49,-20,34,22,-18,-78,-11,16,28,-90,-39,9,50,-91,-86,-98,49,-57,31,18,7,-70,35,-5,-40,-48,-28,-89,39,-29,44,-27,-20,-39,-56,-58,47,-58,-85,39,3,44,-64,-65,-58,-63,38,42,3,10,21,34,-8,-3,-100,-25,-23,-23,-49,-25,-57,-92,8,-73,32,-17,-31,-26,46,44,-73,43,9,-24,36,44,-90,-3,7],[36,27,-81,-41,11,-95,-39,3,17,-88,-95,4,31,17,-53,-61,39,-99,15,-17,40,-28,-26,-21,-79,-17,-35,-7,5,-41,26,-34,-57,-70,-4,-11,-59,-11,3,-91,-67,-46,-49,-93,-60,-24,-81,-46,-66,-54,-9,-11,-71,-32,-97,26,-91,-23,-20,-48,-68,-95,-2,-24,1,45,-29,37,-42,43,-78,-38,-6,-97,-55,43,9,-65,-34,-74,-100,-10,-86,25,-93,-48,-25,5,-46,28,32,-86,-33,-90,19,-49,-67,-45,1,17,24,11,10,-54,-87,-72,7,-11,5,-9,-45,-57,-40,-92,-44,-57,5,-9,-29,-46,46,-75,21,-79,-75,-29,-13,28,14,-25],[-99,-68,-16,-60,-14,45,30,-20,18,-18,27,-6,-41,-81,-98,24,0,-98,-77,20,-41,17,2,-90,19,1,-38,20,6,-50,21,0,-81,-98,-38,11,-27,-72,-96,41,-47,8,29,3,-47,-23,-19,33,7,-44,-55,-38,-15,10,-81,-66,0,-77,20,-90,-33,-8,-82,-15,-20,23,-7,-27,43,-66,-64,-59,5,-69,36,-42,-84,-41,-3,-30,6,23,34,-74,-20,-68,-66,-76,-70,-44,22,-42,4,-81,46,1,-71,-78,-51,-87,16,-92,37,-28,41,-61,-32,-32,8,-33,-59,-89,-52,-35,-74,-13,38,-37,28,2,-60,-86,-71,7,-63,5,-23,-76,3,-10],[-3,11,12,-63,-9,-35,-69,-33,-8,-92,-48,-8,29,22,35,49,17,-10,-68,47,-42,-91,-36,10,-79,7,-35,-92,-1,-8,-34,-74,-5,47,0,37,-38,27,-8,-90,20,-59,-25,-63,-43,-14,-7,-53,-75,-12,-100,32,-64,-37,-73,-12,23,-98,-33,-21,38,-84,-56,48,37,2,-95,-65,10,-82,50,-4,47,-24,-19,14,-86,33,18,-18,-37,26,-9,21,-5,-51,-55,-12,-4,-33,36,13,46,-54,-100,-82,-7,-89,37,-32,-9,4,-59,-23,-21,-97,-26,-97,-77,7,-6,-59,-41,21,-75,-5,2,-19,26,-93,-37,50,-18,-13,-78,-26,-75,-72,29,-25],[2,8,-74,15,-19,-26,47,-22,32,17,-53,-84,-13,-17,50,-10,-3,37,-18,-49,-2,-5,-82,-96,-89,-98,-31,-74,-24,6,14,-90,-5,-5,21,-39,1,24,-15,-94,-13,29,38,-72,-31,-74,30,-25,30,-85,13,29,-86,36,-19,-19,29,-34,-9,-54,-26,-81,-93,12,39,-15,-19,-30,31,2,21,-21,-50,-56,-23,-65,-91,29,16,-57,-41,16,-33,12,-66,-10,-19,-97,-18,-58,30,-44,-45,35,12,10,-18,-22,-96,-25,-83,-63,4,-25,36,-12,-66,-44,-27,-6,44,-42,-95,-50,-93,-76,-23,-85,-57,-78,50,-90,-13,-29,-98,-47,-96,-30,-45,-71]]
print s.calculateMinimumHP(d)