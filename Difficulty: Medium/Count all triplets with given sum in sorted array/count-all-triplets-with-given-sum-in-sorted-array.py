
class Solution:
    def countTriplets(self, arr, target):
        # code here
        count = 0
        n = len(arr)

        for i in range(n - 2):
            l = i + 1
            r = n - 1
            while l < r:
                curr_sum = arr[i] + arr[l] + arr[r]
                if curr_sum == target:
                    if arr[l] == arr[r]:
                        count += (r - l + 1) * (r - l) // 2
                        break
                    else:
                        left_count = 1
                        right_count = 1

                        while l + 1 < r and arr[l] == arr[l + 1]:
                            left_count += 1
                            l += 1

                        while r - 1 > l and arr[r] == arr[r - 1]:
                            right_count += 1
                            r -= 1
                        
                        count += left_count * right_count
                        l += 1
                        r -= 1
                elif curr_sum < target:
                    l += 1
                else:
                    r -= 1
        return count



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        target = int(input())
        ob = Solution()
        ans = ob.countTriplets(arr, target)
        print(ans)
        print("~")
# } Driver Code Ends