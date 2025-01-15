# User function Template for python3

class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        prefix_sum = maxi = 0
        prefix_map = {}
        
        for i in range(len(arr)):
            prefix_sum += arr[i]
            if prefix_sum == k:
                maxi = i + 1
            if (prefix_sum - k) in prefix_map:
                maxi = max(maxi, i - prefix_map[prefix_sum - k])
        
            if prefix_sum not in prefix_map:
                prefix_map[prefix_sum] = i
        
        return maxi            
                
                
        
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        print(ob.longestSubarray(arr, k))
        tc -= 1
        print("~")
# } Driver Code Ends