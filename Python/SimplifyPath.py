class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        stack = []
        list = ''
        if path[-1] != '/':
            path = path + '/'
        for i in range(0,len(path)):
            if path[i] != '/' and i != (len(path) -1):
                list = list + path[i]
            else:
                if list == '.' or list == '':
                    list = ''
                elif list == '..':
                    if len(stack)>0:
                        stack.pop() 
                    list = ''
                else:
                    list = list + '/'
                    stack.append(list)
                    list = ''
        s = ''
        for j in range(0,len(stack)):
            s = s + stack[j]
        return '/' + s[0:-1]
        
        
        
ss = Solution()
str = '/a/./b/../../c/'
print ss.simplifyPath(str)
str = '/../'
print ss.simplifyPath(str)
str = '/home//foo/'
print ss.simplifyPath(str)
str = '/...'
print ss.simplifyPath(str)