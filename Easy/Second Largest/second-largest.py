#User function Template for python3
class Solution:
	def print2largest(self,arr, n):
		# code here
        max_element = float('-inf')
        second_max_element = float('-inf')
        for num in arr:
            if num>max_element:
                second_max_element = max_element;
                max_element = num;
            elif num!=max_element and num >second_max_element:
                second_max_element = num
        return second_max_element if second_max_element != float('-inf') else -1

#{ 
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.print2largest(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends