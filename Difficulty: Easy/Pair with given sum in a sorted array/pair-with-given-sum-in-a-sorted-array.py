#User function Template for python3


class Solution:
    def countPairs (self, arr, target) : 
        #Complete the function

        l, r = 0, len(arr) - 1
        count = 0

        while l < r:
            curr_sum = arr[l] + arr[r]
            if curr_sum == target:
                if arr[l] == arr[r]:
                    n = r - l + 1
                    count += (n * (n - 1)) // 2
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
#Initial Template for Python 3


def main():
    import sys
    input = sys.stdin.read
    data = input().split('\n')

    t = int(data[0].strip())
    index = 1

    for _ in range(t):
        arr = list(map(int, data[index].strip().split()))
        index += 1
        target = int(data[index].strip())
        index += 1

        res = Solution().countPairs(arr, target)
        print(res)
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends