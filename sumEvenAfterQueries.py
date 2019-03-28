class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        result = []

        su = 0

        for x in A:
            if x % 2 == 0:
                su += x

        for val, index in queries:
            if A[index] % 2 == 0:
                su -= A[index]
            A[index] += val
            if A[index] % 2 == 0:
                su += A[index]
            result.append(su)
        return result
