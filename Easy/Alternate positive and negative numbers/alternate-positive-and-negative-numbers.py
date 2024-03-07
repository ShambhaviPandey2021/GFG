#User function Template for python3

class Solution:
    def rearrange(self,arr, n):
        # code here
        listPositive, listNegative = [], []
        
        for num in arr:
            if num >= 0:
                listPositive.append(num)
            else:
                listNegative.append(num)
    
        pos, neg, index = 0, 0, 0
        while pos < len(listPositive) and neg < len(listNegative):
            arr[index] = listPositive[pos]
            index += 1
            pos += 1
            arr[index] = listNegative[neg]
            index += 1
            neg += 1
        
   
        while pos < len(listPositive):
            arr[index] = listPositive[pos]
            index += 1
            pos += 1
        
        while neg < len(listNegative):
            arr[index] = listNegative[neg]
            index += 1
            neg += 1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	tc = int(input())
	while tc > 0:
		n = int(input())
		arr = list(map(int, input().strip().split()))
		ob = Solution()
		ob.rearrange(arr, n)
		for x in arr:
			print(x, end=" ")
		print()
		tc -= 1

# } Driver Code Ends