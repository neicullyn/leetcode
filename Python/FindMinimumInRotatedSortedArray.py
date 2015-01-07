class Solution:
    # @param num, a list of integer
    # @return an integer
    
    def findMin(self, num):
        left = 0
        right = len(num)
        mid = (left + right)/2
        a = num[mid] - num[left]
        b = num[right-1] - num[mid]
        
        if a > 0 and b > 0:
            return num[0]
        
        while right - left > 4:
            if a < 0:
                right = mid + 1
            else:
                left = mid                   
            mid = (left + right)/2
            a = num[mid] - num[left]
            b = num[right-1] - num[mid]
            
        m = num[left]            
        for i in range(left+1, right):
            if m > num[i]:
                m = num[i]
        return m
        
        
        
      
s = Solution()  
num = [4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,0,1,2,3]
print s.findMin(num)
num = range(0,13)
print s.findMin(num)