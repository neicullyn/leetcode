class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        n = len(A)
        if n==1 :
            return True
        if A[0] == 0:
            return False
        for i in range(1, len(A)-1):
            A[i] = max(A[i-1]-1, A[i])
            if A[i] == 0:
                return False
        return True
            
    
s = Solution()
A = [2, 3, 1, 1, 4]
print s.canJump(A)
A = [3, 2, 1, 0, 4]
print s.canJump(A)