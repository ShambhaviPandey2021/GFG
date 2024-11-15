#User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        first_max = -1
        second_max = -1
        for num in arr:
            if num > first_max:
                second_max = first_max
                first_max = num
            elif num > second_max and num != first_max:
                second_max = num
        return second_max

#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")
# } Driver Code Ends