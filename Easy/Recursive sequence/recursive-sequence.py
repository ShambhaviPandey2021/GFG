#User function Template for python3

class Solution:
    def sequence(self, n):
        # code here
        
        result = 0
        mod = 10**9 + 7
        start =  1
        for i in range(n):
            end = start + i
            product = 1
            while (start <= end):
                product = (product * start) % mod
                start += 1
            result = (result + product)% mod
        return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        print(ob.sequence(N))
# } Driver Code Ends