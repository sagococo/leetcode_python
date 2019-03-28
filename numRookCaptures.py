class Solution:

    def searchUp(self):
        y = self.y - 1
        while y >= 0:
            if self.dash[self.x][y] == '.':
                y -= 1
                continue
            elif self.dash[self.x][y] == 'B':
                return False
            elif self.dash[self.x][y] == 'p':
                return True
        return False

    def searchDown(self):
        y = self.y + 1
        while y < self.row:
            if self.dash[self.x][y] == '.':
                y += 1
                continue
            elif self.dash[self.x][y] == 'B':
                return False
            elif self.dash[self.x][y] == 'p':
                return True
        return False

    def searchLeft(self):
        x = self.x - 1
        while x >= 0:
            if self.dash[x][self.y] == '.':
                x -= 1
                continue
            elif self.dash[x][self.y] == 'B':
                return False
            elif self.dash[x][self.y] == 'p':
                return True
        return False

    def searchRight(self):
        x = self.x + 1
        while x < self.collum:
            if self.dash[x][self.y] == '.':
                x += 1
                continue
            elif self.dash[x][self.y] == 'B':
                return False
            elif self.dash[x][self.y] == 'p':
                return True
        return False

    def __init__(self):
        self.row = 0
        self.collum = 0
        self.dash = []
        self.x = 0
        self.y = 0

    def numRookCaptures(self, board: List[List[str]]) -> int:
        self.dash = board
        self.row = len(board)
        self.collum = len(board[0])

        for x in range(0, self.row):
            for y in range(0, self.collum):
                if board[x][y] == 'R':
                    self.x = x
                    self.y = y

        count = 0
        if self.searchUp():
            count += 1
        if self.searchDown():
            count += 1
        if self.searchLeft():
            count += 1
        if self.searchRight():
            count += 1
        return count