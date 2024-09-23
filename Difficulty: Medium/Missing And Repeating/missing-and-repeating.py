#User function Template for python3

class Solution:
    def findTwoElement( self,arr): 
        # code here
        S = (n * (n + 1)) // 2
        Sq = (n * (n + 1) * (2 * n + 1)) // 6
    
        Si = 0  
        Sqi = 0  
        for i in range(n):
            Si += arr[i]
            Sqi += arr[i] * arr[i]
       
        X_minus_Y = S - Si 
        X_plus_Y = (Sq - Sqi) // X_minus_Y 
        
       
        miss = (X_minus_Y + X_plus_Y) // 2
        rep = X_plus_Y - miss
        
        return [rep, miss]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findTwoElement(arr)
        print(str(ans[0]) + " " + str(ans[1]))
        tc = tc - 1

# } Driver Code Ends