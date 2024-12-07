class Solution:
    #User function Template for python3
    #Function to count inversions in the array.
    
    def merge_and_count(self, arr, temp, left, mid, right):
        i = left  
        j = mid + 1  
        k = left  
        inv_count = 0

        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp[k] = arr[i]
                i += 1
            else:
                temp[k] = arr[j]
            
                inv_count += (mid - i + 1)
                j += 1
            k += 1

        while i <= mid:
            temp[k] = arr[i]
            i += 1
            k += 1

        while j <= right:
            temp[k] = arr[j]
            j += 1
            k += 1
        for i in range(left, right + 1):
            arr[i] = temp[i]

        return inv_count

    def merge_sort_and_count(self, arr, temp, left, right):
        inv_count = 0

        if left < right:
            mid = (left + right) // 2

            inv_count += self.merge_sort_and_count(arr, temp, left, mid)

            inv_count += self.merge_sort_and_count(arr, temp, mid + 1, right)

            inv_count += self.merge_and_count(arr, temp, left, mid, right)

        return inv_count
    def inversionCount(self, arr):
        # Your Code Here
        n = len(arr)
        temp = [0] * n
        return self.merge_sort_and_count(arr, temp, 0, n - 1)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a))
        print("~")

# } Driver Code Ends