
class Solution:
    def maxWater(self, arr):
        # code here
        n = len(arr)
        if n <= 2:
            return 0
            
        l_max = [0] * n
        r_max = [0] * n
        
        l_max[0] = arr[0]
        for i in range(1, n):
            l_max[i] = max(l_max[i - 1], arr[i])
        
        r_max[n - 1] = arr[n - 1]
        for i in range(n - 2, -1, -1):
            r_max[i] = max(r_max[i + 1], arr[i])
        
        trapped_water = 0
        for i in range(n):
            trapped_water += max(0, min(l_max[i], r_max[i]) - arr[i])
        
        return trapped_water

#{ 
 # Driver Code Starts
#Initial template for Python 3

import math


def main():
    t = int(input())
    while (t > 0):

        arr = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.maxWater(arr))

        t -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends