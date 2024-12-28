#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


# } Driver Code Ends
#User function Template for python3
class Solution:
    def findTriplets(self, arr):
        # Your code here
        n = len(arr)
        st = set()
        mp = {}
        for i in range(n):
            for j in range(i + 1, n):
                if arr[i] + arr[j] not in mp:
                    mp[arr[i] + arr[j]] = []
                mp[arr[i] + arr[j]].append((i, j))

        for i in range(n):
            req = -arr[i]
            if req in mp:
                for it in mp[req]:
                    if i != it[0] and i != it[1]:
                        curr = [i, it[0], it[1]]
                        curr.sort()
                        st.add(tuple(curr))  
        ans = [list(triplet) for triplet in st]
        return ans


#{ 
 # Driver Code Starts.

def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        ob = Solution()
        res = ob.findTriplets(A)
        res = sorted(res)
        if len(res) == 0:
            print('[]')
        for i in range(len(res)):
            for j in range(len(res[i])):
                print(res[i][j], end=" ")
            print("")
        print('~')
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends