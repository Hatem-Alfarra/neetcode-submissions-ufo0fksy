class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        maxRow = len(matrix)
        maxCol = len(matrix[0]) # Assuming square matrix
        self.sumMatrix = [[0]*(maxCol+1) for _ in range(maxRow+1)]

        for i in range(maxRow):
            rowSum = 0
            for j in range(maxCol):
                rowSum += matrix[i][j]
                self.sumMatrix[i+1][j+1] = rowSum + self.sumMatrix[i][j+1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = self.sumMatrix[row2+1][col2+1] - self.sumMatrix[row1][col2+1] - self.sumMatrix[row2+1][col1] + self.sumMatrix[row1][col1]
        return res
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)