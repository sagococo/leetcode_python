class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        n = len(A[0])

        result = []

        for x in range(n):
            row = []

            for y in A:
                row.append(y[x])

            result.append(row)

        return result