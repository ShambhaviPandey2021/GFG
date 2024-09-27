#User function Template for python3

from collections import deque
from typing import List

class Solution:
    
    #Function to find maximum of each subarray of size k.
    def max_of_subarrays(self,k,arr):
        
        #code here


        ans = []
        dq = deque()
        
        # Process the first 'k' elements
        for i in range(k):
            while dq and arr[dq[-1]] <= arr[i]:
                dq.pop()
            dq.append(i)
    
        ans.append(arr[dq[0]])
    
        # Process the remaining elements
        for i in range(k, len(arr)):
            # Remove elements not in the current window
            if dq[0] <= i - k:
                dq.popleft()
    
            # Include current element and maintain decreasing order
            while dq and arr[dq[-1]] <= arr[i]:
                dq.pop()
    
            dq.append(i)
            
            ans.append(arr[dq[0]])
    
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import deque

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        k = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        res = ob.max_of_subarrays(k, arr)
        for i in range(len(res)):
            print(res[i], end=" ")
        print()

# } Driver Code Ends