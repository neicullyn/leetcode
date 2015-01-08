class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        buf = ''
        stack = []
        for i in range(len(s)):
            if s[i] == ' ':
                stack.append(buf)
                buf = ''
            else:
                buf = buf + s[i]
        stack.append(buf)
        buf = ''
        while len(stack) > 0:
            s = stack.pop()
            if len(s) > 0:
                buf = buf + s + ' '
        return buf[0:len(buf)-1]

s = Solution()
str = 'the sky is blue'
print str
print s.reverseWords(str)

str = ' '
print '"' + s.reverseWords(str) + ''