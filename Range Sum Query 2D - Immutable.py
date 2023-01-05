class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row,col = len(matrix), len(matrix[0])
        a = []
        for i in range(row + 1):
            a += [[0] * (col + 1)]
        self.matrix = a
        for r in range(row):
            prefix_sum = 0
            for c in range(col):
                prefix_sum += matrix[r][c]
                above = self.matrix[r][c+1]
                self.matrix[r+1][c+1] = prefix_sum + above
        print(self.matrix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1,col1,row2,col2 = row1+1,col1+1,row2+1,col2+1
        bottom_right = self.matrix[row2][col2]
        top_right = self.matrix[row1-1][col2]
        bottom_left = self.matrix[row2][col1-1]
        top_left = self.matrix[row1-1][col1-1]
        return bottom_right - top_right - bottom_left + top_left


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)