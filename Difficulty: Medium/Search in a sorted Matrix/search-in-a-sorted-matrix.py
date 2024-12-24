
#User function Template for python3

class Solution:
    
    #Function to search a given number in row-column sorted matrix.
    def searchMatrix(self, mat, x): 
    	# code here
        n = len(mat)       
        m = len(mat[0])    
        
        low, high = 0, n * m - 1
        while low <= high:
            mid = (low + high) // 2
            mid_v = mat[mid // m][mid % m]  
            if mid_v == x:
                return True  
            elif mid_v < x:
                low = mid + 1  
            else:
                high = mid - 1  
        return False 
    	



#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1
    for _ in range(t):
        r = int(data[index])
        c = int(data[index + 1])
        index += 2
        matrix = []
        for i in range(r):
            row = list(map(int, data[index:index + c]))
            matrix.append(row)
            index += c
        x = int(data[index])
        index += 1
        ob = Solution()
        if ob.searchMatrix(matrix, x):
            print("true")
        else:
            print("false")
        print("~")
# } Driver Code Ends