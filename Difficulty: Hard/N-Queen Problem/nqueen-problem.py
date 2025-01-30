#User function Template for python3

class Solution:
    def solve(self, colo, n, ans, sol, col, ldiag, rdiag):
        for i in range(n):
            if colo == n:
                ans.append(sol[:])  #storing  the current solution
                return

            if not col[i] and not ldiag[colo - i + n - 1] and not rdiag[i + colo]:
                sol.append(i + 1)  # Placing our queen
                col[i] = True
                ldiag[colo - i + n - 1] = True
                rdiag[i + colo] = True

                self.solve(colo + 1, n, ans, sol, col, ldiag, rdiag) 

                sol.pop()  # Backtrack 
                col[i] = False
                ldiag[colo - i + n - 1] = False
                rdiag[i + colo] = False

    def nQueen(self, n):
        # code here
        col = [False] * n
        ldiag = [False] * (2 * n - 1)
        rdiag = [False] * (2 * n - 1)
        ans = []
        sol = []
        self.solve(0, n, ans, sol, col, ldiag, rdiag)
        return ans




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        ob = Solution()
        ans = ob.nQueen(n)
        if (len(ans) == 0):
            print("-1")
        else:
            ans.sort()
            for i in range(len(ans)):
                print("[", end="")
                for j in range(len(ans[i])):
                    print(ans[i][j], end=" ")
                print("]", end=" ")
            print()

        print("~")

# } Driver Code Ends