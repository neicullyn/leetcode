class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        r = A[0]
        for i in range(1, len(A)):
            r = r ^ A[i]
        return r
        pass
    
s = Solution()
A = [1, 1, 2, 2, 5, 5, 4, 3, 3]
print s.singleNumber(A)