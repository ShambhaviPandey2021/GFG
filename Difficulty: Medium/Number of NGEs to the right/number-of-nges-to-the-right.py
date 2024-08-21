#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def count_NGEs(self, N, arr, queries, indices):
        # Code here
      
        res = []
        for i in range(len(indices)):
            count = 0
            start_index = indices[i]
            
            for j in range(start_index + 1,len(arr)):
                if arr[j ]>arr[start_index]:
                    count+= 1
                
            res.append(count)
     
        return res
        
#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        arr = list(map(int, input().split()))
        queries = int(input())
        indices = list(map(int, input().split()))
        ob = Solution()
        NGEs = ob.count_NGEs(N, arr, queries, indices)
        for val in NGEs:
            print(val, end = ' ')
        print()
# } Driver Code Ends