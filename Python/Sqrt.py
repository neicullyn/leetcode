class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        # y = sqrt x
        # y^2 = x
        # f(y) = x - y^2 
        # f'(y) = -2y 
        # y1 = y0 - 0.5 y0
        y = x * 0.5
        yold = 0
        
        while abs(y - yold) > 0.25:
#             print y
            yold = y
            y = y - (x - y * y)/(-2 * y)
            
        
        return int(y)
        


s = Solution()
print s.sqrt(16)
print s.sqrt(17)
print s.sqrt(260)        