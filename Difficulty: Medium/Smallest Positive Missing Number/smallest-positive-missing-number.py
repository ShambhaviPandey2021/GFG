#User function Template for python3

class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr):
        #Your code here
        n = len(arr)
        for i in range(n):
            if arr[i] <= 0 or arr[i] > n:
                arr[i] = 0

        for i in range(n):
            val = abs(arr[i])
            if 1 <= val <= n:
         
                if arr[val - 1] > 0:
                    arr[val - 1] = -arr[val - 1]
                elif arr[val - 1] == 0:
                    arr[val - 1] = -(n + 1)  
        for i in range(n):
            if arr[i] >= 0:
                return i + 1

        return n + 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.missingNumber(arr))
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends