#User function Template for python3


class Solution:

    def aggressiveCows(self, stalls, k):

        def canPlaceCows(stalls, k, dist):
            count_cows = 1  
            last_position = stalls[0]

            for i in range(1, len(stalls)):
                if stalls[i] - last_position >= dist:
                    count_cows += 1  
                    last_position = stalls[i]
                    if count_cows == k:  
                        return True
            return False
        
        stalls.sort()

      
        low = 1  
        high = stalls[-1] - stalls[0]  
        result = 0

        while low <= high:
            mid = (low + high) // 2  

            if canPlaceCows(stalls, k, mid):
                result = mid  
                low = mid + 1 
            else:
                high = mid - 1 

        return result




#{ 
 # Driver Code Starts
#Initial Template for Python 3
import bisect
#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.aggressiveCows(A, D)
        print(ans)
        print("~")
# } Driver Code Ends