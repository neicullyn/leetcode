class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def unique(self, num):
        for i in range(0, len(num)-1):
            if num[i] == num[i+1]:
                return False
        return True
    
    def fourSum(self, num, target):
        n = len(num)
        r = range(n)
        d = dict()
        d2 = dict()
        lst = []
        for i in r:
            for j in range(i+1, n):                
                key = num[i] + num[j]
                if not d.has_key(key):
                    d[key] = []
                d[key].append((i,j))
        sorted_keys = d.keys()
        sorted_keys.sort()
        for k in sorted_keys:
            l = target - k
            if l >= k and d.has_key(l):
                big_set_a = d[k]
                big_set_b = d[l]
                for x in big_set_a:
                    for y in big_set_b:
                        z = list(x + y)
                        z.sort()
                        if self.unique(z):
                            temp = []
                            for i in z:
                                temp.append(num[i])
                            temp.sort()
                            z = tuple(temp)
                            d2[z] = temp
        for x in d2.items():
            lst.append(x[1])
        return lst
                
                

S = [1, 0, -1, 0, -2, 2]
target = 0

print Solution().fourSum(S, target)

S = [0, 0, 0, 0]
target = 0
print Solution().fourSum(S, target)