#User function Template for python3

class Solution:
    def getPairsCount(self, arr, n, k):
        # code here
        frequency_map = {}
        count = 0;
        for i in arr:
            complement = k - i
            if complement in frequency_map:
                count += frequency_map[complement]
            
            frequency_map[i] = frequency_map.get(i,0) + 1
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getPairsCount(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends