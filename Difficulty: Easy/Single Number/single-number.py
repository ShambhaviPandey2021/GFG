#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    
    def getSingle(self,arr):
        # code here
        res = 0
        freq_map = {}
        for item in arr:
            if item in freq_map:
                freq_map[item] += 1
            else:
                freq_map[item] = 1
        for item, freq in freq_map.items():
            if freq%2 != 0:
                return item
     

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        # k= int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.getSingle(arr)
        print(res)
        t -= 1


# } Driver Code Ends