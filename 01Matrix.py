

class Solution:

    def isFull(self, maxtrix):
        for x in range(0, self.row):
            for y in range(0, self.collum):
                if maxtrix[x][y] == -1:
                    return False
        return True


    def set_code(self, matrix, param, x, y):
        if y + 1 < self.collum:
            matrix[x][y + 1] = param
        if y - 1 >= 0:
            matrix[x][y - 1] = param
        if x + 1 < self.row:
            matrix[x + 1][y] = param
        if x - 1 >= 0:
            matrix[x - 1][y] = param
        return matrix

    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        self.row = len(matrix)
        self.collum = len(matrix[0])

        for x in range(0, self.row):
            for y in range(0, self.collum):
                if matrix[x][y] == 1:
                    matrix[x][y] = -1

        code = 0

        while True:
            for x in range(0, self.row):
                for y in range(0, self.collum):
                    if matrix[x][y] == code:
                        new = code + 1
                        matrix = self.set_code(self, matrix, new, x, y)
            code += 1
            if self.isFull(self, matrix):
                break
