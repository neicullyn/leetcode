class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        m = dict(zip(num, range(1, len(num)+1)))
        for i in range(0, len(num)):
            g = m.get(target - num[i])
            if g is not None:
                p = i + 1
                q = g
                if p != q:
                    if p > q:
                        p, q = q, p
                    return p, q
                        

            

num = list({3, 2, 4})
solution = Solution()
print solution.twoSum(num, 6)