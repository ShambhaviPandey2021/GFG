#User function Template for python3

class Solution:
    def nQueen(self, n):
        # code here
        board = [[0 for _ in range(n)] for _ in range(n)]
        results = []
        self.solveNQueens(board, 0, n, results)
        return results
        
        
    def isSafe(self,board,row,col,n):
        
        # checking the column
        for i in range(row):
            if board[i][col] == 1:
                return False
                
        #checking for diagonal left
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        
        #checking the diagonal right
        for i, j in zip(range(row, -1, -1), range(col, n)):
            if board[i][j] == 1:
                return False

        return True
    
    def solveNQueens(self, board, row, n, results):
        if row >= n:
            
            result = []
            for i in range(n):
                for j in range(n):
                    if board[i][j] == 1:
                        result.append(j + 1)  
            results.append(result)
            return
        
        for col in range(n):
            if self.isSafe(board, row, col, n):
           
                board[row][col] = 1
              
                self.solveNQueens(board, row + 1, n, results)
           
                board[row][col] = 0
                
        
            
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        ob = Solution()
        ans = ob.nQueen(n)
        if(len(ans) == 0):
            print("-1")
        else:
            for i in range(len(ans)):
                print("[",end="")
                for j in range(len(ans[i])):
                    print(ans[i][j],end = " ")
                print("]",end = " ")
            print()
                
# } Driver Code Ends