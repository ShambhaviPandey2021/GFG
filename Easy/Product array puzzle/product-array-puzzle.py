#User function Template for python3

class Solution:
    def productExceptSelf(self, nums, n):
        #code here
        result = [1] * n
        product = 1
        for i in range(n):
            result[i] *= product
            product *= nums[i]

        rightProduct = 1
        
 
        for i in range(n - 1, -1, -1):
            result[i] *= rightProduct
            rightProduct *= nums[i]
        
        return result



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())

    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]

        ans=Solution().productExceptSelf(arr,n)
        print(*ans)
# } Driver Code Ends