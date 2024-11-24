#User function Template for python3

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr):
        ##Your code here    
        max_ending_here = arr[0]  
        max_so_far = arr[0]     

        for i in range(1, len(arr)):
            
            max_ending_here = max(arr[i], max_ending_here + arr[i])
           
            max_so_far = max(max_so_far, max_ending_here)

        return max_so_far
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.maxSubArraySum(arr))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends