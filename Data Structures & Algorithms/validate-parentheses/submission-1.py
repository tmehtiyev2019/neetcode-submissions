class Solution:
    def isValid(self, s: str) -> bool:
        par_map = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        stack = []
        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)

            if char in [')', '}', ']']:
                if not stack:
                    return False
                key = stack.pop()
                if par_map[char] != key:
                    return False
        if stack:
            return False
        return True


        # stack[([{}])]
        