class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        r = 0
        while n >= 5:
            r = r + n / 5
            n = n / 5
        return r
    
s=Solution()
print s.trailingZeroes(5)