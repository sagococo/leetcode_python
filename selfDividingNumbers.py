class Solution:

    def isOK(self, n):
        string = str(n)
        for y in string:
            if y == '0':
                return False
            if n%int(y) != 0:
                return False
        return True

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for x in range(left, right+1):
            if self.isOK(x):
                result.append(x)
        return result