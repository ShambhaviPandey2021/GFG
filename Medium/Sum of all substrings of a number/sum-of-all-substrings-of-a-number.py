#User function Template for python3

class Solution:
    #Function to find sum of all possible substrings of the given string.
    def sumSubstrings(self, s):
        MOD = 10**9 + 7
        n = len(s)
        
        result = 0
        position_multiplier = 1
        cumulative_sum = 0
        for i in range(n-1, -1, -1):
            cumulative_sum = (cumulative_sum + int(s[i]) * position_multiplier) % MOD
            result = (result + cumulative_sum) % MOD

            position_multiplier = (position_multiplier * 10 + 1) % MOD
        
        return result

    


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

import sys
sys.setrecursionlimit(10**6)

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        s = str(input())
        ob=Solution()
        print(ob.sumSubstrings(s))
# } Driver Code Ends