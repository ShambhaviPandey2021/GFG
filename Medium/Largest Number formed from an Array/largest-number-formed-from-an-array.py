#User function Template for python3
class Solution:

	def printLargest(self, n, arr):
	    # code here
        def compare(x,y):
            if(x+y>y+x):
                return -1
            elif (x+y<y+x):
                return 1
            else:
                return 0
        arr.sort(key = functools.cmp_to_key(compare))
        largest_number = ''.join(arr)
        largest_number = largest_number.lstrip('0')
        return largest_number if largest_number else '0'


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import functools

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(str, input().strip().split()))
        ob = Solution()
        ans = ob.printLargest(n, arr)
        print(ans)
        tc -= 1

# } Driver Code Ends