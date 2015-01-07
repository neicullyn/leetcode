class Solution:
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        s = ''
        
        if numerator < 0 and denominator > 0:
            numerator = -numerator
            s = s + '-'
            
        if  numerator > 0 and denominator < 0:   
            denominator = - denominator
            s = s + '-' 
            
        q = numerator / denominator
        r = numerator % denominator
        if r == 0:
            return s + str(q)
        else:
            #  5/3 : 1.
            s = s + str(q) + '.'
            cnt = 0            
            lst = []
            mp = dict()
            while 1:
                if r == 0:
                    flag = 1
                    break;
                if mp.has_key(r):
                    flag = 0
                    cnt = mp[r]
                    break;
                mp[r] = cnt
                r = r * 10
                lst.append(r / denominator)
                r = r % denominator
                
                cnt = cnt + 1
                
            if flag == 0:
                for i in range(0, len(lst)):
                    if i == cnt:
                        s = s + '('
                    s = s + str(lst[i])
                s = s + ')'
            else:
                for i in range(0, len(lst)):
                    s = s + str(lst[i])
            return s
            
            
            
            
        
        
s = Solution()
print s.fractionToDecimal(1, 1)
print s.fractionToDecimal(1, 2)
print s.fractionToDecimal(2, 3)
print s.fractionToDecimal(1, 6)