class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        r1 = 0
        r2 = 0
        for i in range(0, len(A)):
            #00->01->10->00
            #r1=1 -> r1=0
            #r1=0 -> r1=r2
            #r2=0 -> r2=~r1
            #r2=1 -> r2=0
            r1, r2 = ((~r1) & r2 & A[i]) | (r1 & ~A[i]), ((~r2) & (~r1) & A[i]) | (r2 & ~A[i]) 
        return r2
    
s = Solution()
A = [1, 1, 1, 2]
print s.singleNumber(A)

