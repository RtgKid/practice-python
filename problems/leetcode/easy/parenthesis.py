class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in s:
            if i in ['(', '{', '[']:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                p = stack.pop()
                if i == ')' and p != '(':
                    return False
                if i == '}' and p != '{':
                    return False
                if i == ']' and p != '[':
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False