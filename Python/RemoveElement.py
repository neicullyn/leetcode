class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        j = 0
        for i in range(0,len(A)):
            if A[i] != elem:
                A[j] = A[i]
                j += 1
        return j
                
s = Solution()
A = [1,1,2,2,3,3,3,4,4,5]
print s.removeElement(A, 2)
print A