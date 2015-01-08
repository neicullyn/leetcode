class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        cnt = [0, 0, 0]
        for i in range(len(A)):
            cnt[A[i]] += 1
        for i in range(cnt[0]):
            A[i] = 0
        base = cnt[0]
        for i in range(cnt[1]):
            A[base+i] = 1
        base = cnt[0] + cnt[1]
        for i in range(cnt[2]):
            A[base+i] = 2

s = Solution()
l = [0, 1, 1, 0, 2, 2]
s.sortColors(l)
print l