#User function Template for python3

class Solution:
    def totalFruits(self,arr):
        # Code here
        fruit_count = {}
        l = 0
        maxlen = 0

        for r in range(len(arr)):
            fruit_count[arr[r]] = fruit_count.get(arr[r], 0) + 1
            
            while len(fruit_count) > 2:
                fruit_count[arr[l]] -= 1
                if fruit_count[arr[l]] == 0:
                    del fruit_count[arr[l]]
                l += 1
            
            maxlen = max(maxlen, r - l + 1)
        
        return maxlen



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        # N = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.totalFruits(arr)
        print(res)

# } Driver Code Ends