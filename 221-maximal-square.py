class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        max_edge = 0

        for i  in range(len(matrix)):
            matrix[i] = [int(x) for x in matrix[i]]

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r == 0 or c == 0:
                    max_edge = max(max_edge, matrix[r][c])
                elif matrix[r][c] == 1:
                    matrix[r][c] = min(matrix[r-1][c], matrix[r][c-1], matrix[r-1][c-1]) + 1
                    max_edge = max(max_edge, matrix[r][c])

        return max_edge ** 2

