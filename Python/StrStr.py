class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):
        m = len(haystack)
        n = len(needle)
        for i in range(0, m - n + 1):
            flag = 1
            for j in range(0, n):
                if haystack[i+j] != needle[j]:
                    flag = 0
                    break
            if flag == 1:
                return i
            else:
                continue
        return -1
s = Solution()
haystack = 'abcda'
needle = 'cd'
print s.strStr(haystack, needle)