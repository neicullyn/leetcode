class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        n = len(A)
        if n > 0:
            j = 1
            for i in range(1,n):
                if A[i] != A[j-1]:
                    A[j] = A[i]
                    j += 1
            return j
    
s = Solution()
A = [1,1,2,2,3,3,3,4,4,5]
print s.removeDuplicates(A)
print A