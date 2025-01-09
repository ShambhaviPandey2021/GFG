#User function Template for python3
class Solution:
    def subarraySum(self, arr, target):
        # code here
        start = 0
        curr_sum = 0

        for end in range(len(arr)):
            curr_sum += arr[end]  
            while curr_sum > target and start <= end:
                curr_sum -= arr[start]
                start += 1
            if curr_sum == target:
                return [start + 1, end + 1]  
        return [-1]

#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        d = int(input().strip())
        ob = Solution()
        result = ob.subarraySum(arr, d)
        print(" ".join(map(str, result)))
        tc -= 1
        print("~")

# } Driver Code Ends