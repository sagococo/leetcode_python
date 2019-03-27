class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0;
        while True:
            if x % 2 != y % 2:
                count += 1
            x = int(x // 2)
            y = int(y // 2)
            if x == 0 and y == 0:
                break

        return count


if __name__ == '__main__':
    s = Solution()
    s.hammingDistance(1, 4)
