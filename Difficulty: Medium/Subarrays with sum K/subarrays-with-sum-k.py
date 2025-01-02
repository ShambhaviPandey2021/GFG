#User function Template for python3

class Solution:
    def countSubarrays(self, arr, k):
        # code here
        count = 0
        p_sum = 0
        sum_count = {0: 1}  
        
        for num in arr:
            p_sum += num  
            if p_sum - k in sum_count:
                count += sum_count[p_sum - k]
            
            sum_count[p_sum] = sum_count.get(p_sum, 0) + 1
        
        return count




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
        res = ob.countSubarrays(arr, k)
        print(res)
        print("~")

# } Driver Code Ends