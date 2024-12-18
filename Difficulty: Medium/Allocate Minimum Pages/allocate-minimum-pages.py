class Solution:
    #Function to find minimum number of pages.
    def findPages(self, arr, k):
        #code here
        n = len(arr)
        if k > n:
            return -1

        def isFeasible(max_pages):
            st_count = 1
            curr_pages = 0

            for pages in arr:
                if pages > max_pages:
                    return False
                if curr_pages + pages > max_pages:
                    st_count += 1
                    curr_pages = pages
                    if st_count > k:
                        return False
                else:
                    curr_pages += pages
            return True

        l, h = max(arr), sum(arr)
        result = h

        while l <= h:
            mid = (l + h) // 2
            if isFeasible(mid):
                result = mid
                h = mid - 1
            else:
                l = mid + 1

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
        ans = ob.findPages(A, D)
        print(ans)
        print("~")

# } Driver Code Ends