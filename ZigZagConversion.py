class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s

        index = 0
        direction = 1

        string = []

        for x in range(0, numRows):
            string.append('')

        for x in s:
            string[index] += x

            if index + direction == numRows:
                direction = -1

            if index + direction < 0:
                direction = 1

            index += direction

        result = ''
        for x in string:
            result += x
        return result
