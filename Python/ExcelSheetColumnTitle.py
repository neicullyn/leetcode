class Solution:
    # @return a string
    def convertToTitle(self, num):
        base = 1
        s = []
        str = ''
        while sum(s)*26 < num:
            s.append(base)
            base = base * 26
            
        while len(s)>0:
            base = s.pop()
            p = num / base
            q = num % base

            if base ==1 or q >= s[-1]:
                num = q
            else:
                p = p - 1
                num = base                
            str = str + (chr(ord('A')+p-1))            
        return str

s = Solution()
print s.convertToTitle(700)