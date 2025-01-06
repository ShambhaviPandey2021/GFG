#User function Template for python3
class Solution:
    def sumClosest(self, arr, target):
        # code here
        if len(arr) < 2:
            return []

        arr.sort()
        n = len(arr)
        l, r = 0, n - 1
        closest_sum = float('inf')
        best_pair = []

        while l < r:
            curr_sum = arr[l] + arr[r]
            abs_diff = abs(arr[r] - arr[l])

            if abs(target - curr_sum) < abs(target - closest_sum) or (
                abs(target - curr_sum) == abs(target - closest_sum) and abs_diff > abs(best_pair[1] - best_pair[0])):
                closest_sum = curr_sum
                best_pair = [arr[l], arr[r]]

            if curr_sum < target:
                l += 1
            else:
                r -= 1

        return best_pair



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input().strip())
    while t > 0:
        arr = list(map(int, input().strip().split()))
        target = int(input().strip())
        ob = Solution()
        ans = ob.sumClosest(arr, target)
        if not ans:
            print("[]")
        else:
            print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends