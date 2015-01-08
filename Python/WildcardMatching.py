class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def _isMatch(self, s, s_begin, p, p_begin):
#         print len(s), s_begin, len(p), p_begin
#         print '[',s[s_begin:],'] [', p[p_begin:],']'
        
        if s_begin >= len(s) and p_begin >= len(p):
            return True
        
        if s_begin >= len(s):
            if p[p_begin] == '*':
                return self._isMatch(s, s_begin, p, p_begin+1)
            else:
                return False
        
        if p_begin >= len(p):
            return False
        
        if s[s_begin] == p[p_begin]:
            return self._isMatch(s, s_begin+1, p, p_begin+1)
        
        if p[p_begin] == '?':
            return self._isMatch(s, s_begin+1, p, p_begin+1)
        
        if p[p_begin] == '*':
            while p_begin < len(p) and p[p_begin] == '*':
                p_begin += 1
                
            while s_begin <= len(s):
                if self._isMatch(s, s_begin, p, p_begin):
                    return True
                s_begin = s_begin + 1    
                
        return False
    
    def isMatch(self, s, p):
        return self._isMatch(s, 0, p, 0) 

print not Solution().isMatch('aa', 'a')
print Solution().isMatch('', '')
print not Solution().isMatch('aaa', 'aa')
print Solution().isMatch('aa', '*')
print Solution().isMatch('aa', 'aa')
print Solution().isMatch('cab', 'c*')
print not Solution().isMatch('cab', 'a*b')
print Solution().isMatch('cab', 'c?b')
print not Solution().isMatch('cab', 'c*a')
