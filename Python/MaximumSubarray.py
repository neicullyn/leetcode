class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        for i in range(1, len(A)):
            A[i] = max(A[i], A[i] + A[i-1])
        print A
        return max(A)
    
A = [-2,1,-3,4,-1,2,1,-5,4]
print Solution().maxSubArray(A)
A = [1]
print Solution().maxSubArray(A)
        