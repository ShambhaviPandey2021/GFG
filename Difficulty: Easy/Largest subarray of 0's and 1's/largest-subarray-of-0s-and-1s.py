class Solution:
    def maxLen(self, arr):
        # code here
        arr = [-1 if x == 0 else 1 for x in arr]
        
        sum_map = {}
        cumulative_sum = 0
        max_length = 0
        
        for i in range(len(arr)):
            cumulative_sum += arr[i]
            if cumulative_sum == 0:
                max_length = i + 1
            
            if cumulative_sum in sum_map:
                max_length = max(max_length, i - sum_map[cumulative_sum])
            else:
                sum_map[cumulative_sum] = i
        
        return max_length


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    a = list(map(int, input().split()))
    s = Solution().maxLen(a)
    print(s)

# } Driver Code Ends