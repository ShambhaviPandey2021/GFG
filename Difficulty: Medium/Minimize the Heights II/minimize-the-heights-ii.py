#User function Template for python3

class Solution:
    def getMinDiff(self, arr,k):
        # code here

        arr.sort()
        n = len(arr)
        
        longest = arr[-1]
        shortest = arr[0]
        ans = longest - shortest
        
        for i in range(1, n):
            longest = max(arr[-1] - k, arr[i-1] + k)
            shortest = min(arr[0] + k, arr[i] - k)
            
            if shortest < 0:
                continue
            
            ans = min(ans, longest - shortest)
        
        return ans



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        # n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, k)
        print(ans)
        tc -= 1

# } Driver Code Ends