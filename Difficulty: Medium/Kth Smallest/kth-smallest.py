#User function Template for python3
import heapq

class Solution:

    def kthSmallest(self, arr,k):
        heapq.heapify(arr)
        kth_min = None
        for _ in range(k):
            kth_min = heapq.heappop(arr)
        return kth_min
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    import random
    t = int(input())
    for tcs in range(t):
        # n = int(input())
        arr = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        print(ob.kthSmallest(arr, k))

# } Driver Code Ends