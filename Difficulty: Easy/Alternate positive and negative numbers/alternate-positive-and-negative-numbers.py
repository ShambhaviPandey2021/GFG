#User function Template for python3

class Solution:
    def rearrange(self,arr):
        # code here
        pos = []
        neg = []

        for num in arr:
            if num >= 0:
                pos.append(num)
            else:
                neg.append(num)

        result = []
        i, j = 0, 0
        while i < len(pos) and j < len(neg):
            result.append(pos[i])
            result.append(neg[j])
            i += 1
            j += 1
      
        while i < len(pos):
            result.append(pos[i])
            i += 1

        while j < len(neg):
            result.append(neg[j])
            j += 1
        
        for k in range(len(arr)):
            arr[k] = result[k]
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.rearrange(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends