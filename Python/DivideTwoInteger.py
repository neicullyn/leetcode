from sys import maxint
class Solution:
    # @return an integer
    def _divide(self, dividend, divisor):
        s = 0
        if divisor == 0:
            return maxint
        if dividend < divisor:
            return 0
        pos = 0
        while divisor <= dividend:
            divisor = divisor << 1
            pos += 1
        divisor = divisor >> 1
        pos -= 1
        while pos >= 0:
#             print dividend, divisor, pos, s
            if dividend >= divisor:
                dividend = dividend - divisor
                s = s + (1 << pos)
            divisor = divisor >>1
            pos -= 1
        return s
        
    def divide(self, dividend, divisor):
        sign = 1
        if divisor < 0:
            sign = sign * -1
            divisor = - divisor
        if dividend < 0:
            sign = sign * -1
            dividend = - dividend
        r = sign * self._divide(dividend, divisor)
        if r > 2147483647:
            r = 2147483647
        if r < -2147483648:
            r = -2147483648
        return r

        

s = Solution()
print s.divide(1,1)
print s.divide(9, 8)
print s.divide(121, 11)
print s.divide(-2147483648, -1)