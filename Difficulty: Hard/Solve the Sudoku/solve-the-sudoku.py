#User function Template for python3


class Solution:

    def satisfy(self, board, row, col, num):
        for r in range(9):
            if board[row][r] == num or board[r][col] == num:
                return False

        start_row, start_col = row - row % 3, col - col % 3
        for r in range(3):
            for c in range(3):
                if board[start_row + r][start_col + c] == num:
                    return False

        return True

    def solve(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:  
                    for num in range(1, 10):  
                        if self.satisfy(board, i, j, num):
                            board[i][j] = num  
                            if self.solve(board):  
                                return True
                            board[i][j] = 0
                    return False  
        return True  
        
    # Function to find a solved Sudoku.
    def solveSudoku(self, mat):
        self.solve(mat)

  

    

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1

    for _ in range(t):
        matrix = []
        n = 9
        for i in range(n):
            row = list(map(int, data[index:index + n]))
            matrix.append(row)
            index += n
        obj = Solution()
        obj.solveSudoku(matrix)
        for i in range(n):
            for j in range(n):
                print(matrix[i][j], end=" ")
            print()
        print("~")

# } Driver Code Ends