class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # horizontal check
        for row in board:
            rowContent = []
            for num in row:
                if num == ".":
                    continue 
                if num in rowContent:
                    return False
                rowContent.append(num)
        # vertical check
        for col in range(len(board[0])):
            colContent = []
            for row in board:
                num = row[col]
                if num == ".":
                    continue
                if num in colContent:
                    return False
                colContent.append(num)
        # sub-box check
        boxAddrs = []
        for col in range(0, len(board[0]), 3):
            for row in range(0, len(board), 3):
                boxAddrs.append([row, col])

        for box in boxAddrs:
            row = box[0]
            col = box[1]
            boxContent = []
            
            for i in range(row, row+3):
                for j in range(col, col+3):
                    num = board[i][j]
                    if num == ".":
                        continue
                    if num in boxContent:
                        return False
                    boxContent.append(num)
    
        return True

        
                
