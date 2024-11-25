#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr):
		# code here
        n = len(arr)
        maxi = arr[0]
        mini = arr[0]
        res = arr[0]
        
        for i in range(1, n):
            num = arr[i]
            if num < 0:
                maxi, mini = mini, maxi
            
            maxi = max(num, maxi * num)
            mini = min(num, mini * num)
            res = max(res, maxi)
        
        return res

		
		
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr)
        print(ans)
        tc -= 1

# } Driver Code Ends