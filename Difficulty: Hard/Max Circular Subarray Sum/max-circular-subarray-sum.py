#User function Template for python3

#Complete this function
#Function to find maximum circular subarray sum.
def circularSubarraySum(arr):
    ##Your code here

    def kadane_max(nums):
        max_ending_here = nums[0]
        max_so_far = nums[0]
        for num in nums[1:]:
            max_ending_here = max(num, max_ending_here + num)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far
    def kadane_min(nums):
        min_ending_here = nums[0]
        min_so_far = nums[0]
        for num in nums[1:]:
            min_ending_here = min(num, min_ending_here + num)
            min_so_far = min(min_so_far, min_ending_here)
        return min_so_far
    max_kadane = kadane_max(arr)
    
    total_sum = sum(arr)
    min_kadane = kadane_min(arr)
    circular_max = total_sum - min_kadane
    if max_kadane < 0:
            return max_kadane
    return max(max_kadane, circular_max)
    
    
    
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
import sys

if __name__ == "__main__":
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        print(circularSubarraySum(arr))

        T -= 1

# } Driver Code Ends