class MinStack:
    # @param x, an integer
    # @return an integer
    def __init__(self):
        self.main_stack = []
        self.min_stack = []
        self.cnt_stack = []
        
    def push(self, x):
        self.main_stack.append(x)
        if(len(self.min_stack)>0):
            if x < self.min_stack[-1]:
                self.min_stack.append(x)
                self.cnt_stack.append(1)
            else:
                self.cnt_stack[-1] += 1
        else:
            self.min_stack.append(x)
            self.cnt_stack.append(1)
        

    # @return nothing
    def pop(self):
        self.main_stack.pop()
        if self.cnt_stack[-1]==1:
            self.min_stack.pop()
            self.cnt_stack.pop()
        else:
            self.cnt_stack[-1] -= 1

    # @return an integer
    def top(self):
        return self.main_stack[-1]        

    # @return an integer
    def getMin(self):
        return self.min_stack[-1]
        
s = MinStack()
s.push(1)
s.push(1)
s.push(2)
s.push(3)
s.push(3)
s.push(4)
s.push(2)
s.push(0)
s.push(0)
s.push(3)
s.push(3)

print s.getMin(),s.top()
s.pop()
print s.getMin(),s.top()
s.pop()
print s.getMin(),s.top()
s.pop()
print s.getMin(),s.top()
s.pop()
print s.getMin(),s.top()
s.pop()
print s.getMin(),s.top()
s.pop()
print s.getMin(),s.top()
s.pop()
print s.getMin(),s.top()
s.pop()
print s.getMin(),s.top()
s.pop()
print s.getMin(),s.top()
s.pop()
print s.getMin(),s.top()
s.pop()
