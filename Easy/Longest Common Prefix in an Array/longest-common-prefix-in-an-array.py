#User function Template for python3

class Solution:
    def longestCommonPrefix(self, arr, n):
        # code here
        if not arr:
            return -1
        
        prefix = arr[0] 
    
        for s in arr[1:]:
            i = 0
            while i < len(prefix) and i < len(s) and prefix[i] == s[i]:
                i += 1
            prefix = prefix[:i]  
        
        return prefix if prefix else -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n = int(input())
        arr = [x for x in input().strip().split(" ")]
        
        ob=Solution()
        print(ob.longestCommonPrefix(arr, n))
# } Driver Code Ends