class Solution:
    def smallestSubWithSum(self, a, n, x):
        # Your code goes here 
        min_length = n + 1
        start = 0
        end = 0
        curr_sum = 0

        while end < n:
            while curr_sum <= x and end < n:
                curr_sum += a[end]
                end += 1

            while curr_sum > x and start < n:
                min_length = min(min_length, end - start)
                curr_sum -= a[start]
                start += 1

        if min_length == n + 1:
            return 0
        return min_length



#{ 
 # Driver Code Starts
def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m = sz[0], sz[1]
        a = [int(x) for x in input().strip().split()]
        print(Solution().smallestSubWithSum(a, n, m))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends