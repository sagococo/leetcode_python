class Solution:

    def isNotOK(self, string):
        l = len(string)
        for x in range(1, l):
            if ord(string[x]) - ord(string[x-1]) < 0:
                return True
        return False

    def minDeletionSize(self, A: List[str]) -> int:
        num = len(A)
        length = len(A[0])
        collums = []

        for x in range(0, length):
            string = ''
            for y in range(0, num):
                string += A[y][x]
            collums.append(string)

        count = 0
        for x in collums:
            if self.isNotOK(x):
                count += 1
        return count