
class Solution:
    def maxWater(self, arr):
        # code here

        n = len(arr)
        if n < 2:
            return 0  
        left, right = 0, n - 1
        max_area = 0
        
        while left < right:
            width = right - left
            height = min(arr[left], arr[right])
            current_area = width * height
            
            max_area = max(max_area, current_area)
            
            if arr[left] < arr[right]:
                left += 1
            else:
                right -= 1
        
        return max_area



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