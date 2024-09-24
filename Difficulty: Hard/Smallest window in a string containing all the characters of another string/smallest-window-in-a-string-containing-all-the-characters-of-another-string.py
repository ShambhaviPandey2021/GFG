#User function Template for python3


class Solution:
    
    #Function to find the smallest window in the string s consisting
    #of all the characters of string p.
    def smallestWindow(self, s, p):
        #code here
        pa, sa = [0] * 26, [0] * 26
        pn, sn, find, i, ans = len(p), len(s), 0, 0, ""
        
        for ch in p:
            pa[ord(ch) - ord('a')] += 1
        
        for j in range(sn):
            c = s[j]
            sa[ord(c) - ord('a')] += 1
            if sa[ord(c) - ord('a')] <= pa[ord(c) - ord('a')]:
                find += 1
            
            while find == pn:
                if not ans or j - i + 1 < len(ans):
                    ans = s[i:j+1]
                c = s[i]
                sa[ord(c) - ord('a')] -= 1
                if sa[ord(c) - ord('a')] < pa[ord(c) - ord('a')]:
                    find -= 1
                i += 1
        
        return ans if ans else "-1"



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

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        p=str(input())
        ob = Solution()
        print(ob.smallestWindow(s,p))
# } Driver Code Ends