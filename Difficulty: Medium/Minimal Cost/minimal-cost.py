#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3


from typing import List


class Solution:
    def minimizeCost(self, k, arr):
        # code here
        n = len(arr)
        dp = [float('inf')] * n
        dp[0] = 0
        
        for i in range(n):
            for j in range(1, k + 1):
                if i + j < n:
                    dp[i + j] = min(dp[i + j], dp[i] + abs(arr[i] - arr[i + j]))
        
        return dp[n - 1] 
        
        

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        k= int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.minimizeCost(k,arr)
        print(res)
        t -= 1


# } Driver Code Ends