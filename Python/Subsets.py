class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        lst = []
        stack = []
        
        S.sort()
        n = len(S)
        r = range(n)
        
        stack.append([])
        while len(stack)>0:
            node = stack.pop()
            if len(node) != n:
                a = list(node)
                b = list(node)
                a.append(0)
                b.append(1)
                stack.append(a)
                stack.append(b)
            else:
                temp = []
                for i in r:
                    if node[i] == 1:
                        temp.append(S[i])
                lst.append(temp)
        return lst
        

S = [1, 2, 3]
print Solution().subsets(S)

S = []
print Solution().subsets(S)