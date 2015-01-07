class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        n = len(s)
        base = 1
        r = 0
        for i in range(0,n):
            p = n - i - 1
            r = r + base * (ord(s[p])-ord('A')+1)
            base = base * 26
        return r


s = Solution()
print s.titleToNumber('ACQ')
