class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if n >= 0:
            r = 1
            while n > 0:
                if n & 1:
                    r = r * x
                x = x * x
                n = n >> 1
            return r
        else:
            return self.pow(1.0 / x, -n)
            
s = Solution()
print s.pow(2, 5)
print s.pow(2, -3)