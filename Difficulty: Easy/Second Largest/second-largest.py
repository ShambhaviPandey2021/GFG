#User function Template for python3
class Solution:
    def print2largest(self, arr):
        # Code Here
        if len(arr) < 2:
            return -1
            
        max_1 = float('-inf')
        sec_max = float('-inf')
        
        for i in arr:
            if i > max_1:
                sec_max = max_1
                max_1 = i
            elif i > sec_max and i < max_1:
                sec_max = i
        
        if sec_max == float('-inf'):
            return -1
        return sec_max
        
            


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.print2largest(arr)
        print(ans)

# } Driver Code Ends