'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

'''
#!/usr/bin/env python3


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if self.__opens(c):
                stack.append(c)
            else:
                if not stack:
                    return False
                opening = stack.pop()
                if not self.__matches(opening, c):
                    return False
        return not stack

    def __opens(self, c: str) -> bool:
        return c in ['(', '{', '[']

    def __matches(self, opening: str, closing :str) -> bool:
        matching = {
            '{': '}',
            '[': ']',
            '(': ')',
        }
        return matching[opening] == closing
