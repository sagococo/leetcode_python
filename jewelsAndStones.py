class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        before = len(S)
        for x in range(0, len(J)):
            char = J[x]
            S = S.replace(char, '')

        after = len(S)
        return before - after