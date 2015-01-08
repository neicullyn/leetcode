class Solution:
    # @param s, a string
    # @return an integer
    def numDedodings(self, s, begin):
        if begin >= self.n:
            return 1
        
        if self.cac[begin]!= -1:
            return self.cac[begin]
        
        num = int(s[begin])
        if num < 1 or num >26:
            r = 0
        elif num==1 and begin < (self.n-1):
            r = self.numDedodings(s, begin + 1) + self.numDedodings(s, begin + 2)
        elif num==2 and begin < (self.n-1) and int(s[begin+1])<=6:
            r = self.numDedodings(s, begin + 1) + self.numDedodings(s, begin + 2)
        else:
            r = self.numDedodings(s, begin + 1)
        self.cac[begin] = r
        return r
        
    def numDecodings(self, s):
        self.n = len(s)
        if self.n == 0:
            return 0
        self.d = dict()
        self.cac = [-1 for i in range(self.n)]
        return self.numDedodings(s, 0)
    
s = '12'
print Solution().numDecodings(s)

s = '123'
print Solution().numDecodings(s)

s = '1213'
print Solution().numDecodings(s)