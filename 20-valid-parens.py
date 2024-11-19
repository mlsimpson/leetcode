class Solution:
    def isValid(self, s: str) -> bool:
        # use a stack data structure
        stack = []

        params_hash = {")": "(", "]": "[", "}": "{"}

        for char in s:
            if char in params_hash:
                # check if stack is not empty first
                # check if top of stack is matching open paren
                if stack and stack[-1] == params_hash[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        # return True if and only if stack is empty
        if stack:
            return False

        return True

