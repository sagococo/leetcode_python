class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        index = 0

        result = ''

        for x in S:
            if x == '(':
                index += 1

                if index != 1:
                    result += x

            if x == ')':
                index -= 1

                if index != 0:
                    result += x

        return result