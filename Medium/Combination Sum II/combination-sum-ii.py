#User function Template for python3

class Solution:
    
    def CombinationSum2(self, arr, n, k):
        # code here
        res=set()
        def util(i,k,curr):
            if k==0:
                res.add(tuple(sorted(curr)))
            if k<0 or i>=n:
                return
            for j in range(i,n):
                util(j+1,k-arr[j],curr+(arr[j],))
        util(0,k,())
        return sorted(res)       

#{ 
 # Driver Code Starts
#Initial Template for Python 3

for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    ob = Solution()
    result = ob.CombinationSum2(arr, n, k)
    for row in result:
        print(*row)
    if not result:
        print()

# } Driver Code Ends