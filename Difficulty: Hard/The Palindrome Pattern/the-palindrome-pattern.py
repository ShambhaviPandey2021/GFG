#User function Template for python3

class Solution:
    def pattern(self, arr):
        n = len(arr)
        
        # Helper function to check if a list is a palindrome
        def is_palindrome(lst):
            return lst == lst[::-1]
        
        # Check rows for palindrome
        for i in range(n):
            if is_palindrome(arr[i]):
                return "{} R".format(i)
        
        # Check columns for palindrome
        for j in range(n):
            col = [arr[i][j] for i in range(n)]
            if is_palindrome(col):
                return "{} C".format(j)
        
        return "-1"
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        a = list()
        c = 0
        for i in range(0, n):
            X = list()
            for j in range(0, n):
                X.append(arr[c])
                c += 1
            a.append(X)
        ans = ob.pattern(a)
        print(ans)

# } Driver Code Ends