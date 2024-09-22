#User function Template for python3

class Solution:
	def lps(self, str):
		# code here
        n = len(s)
        p = 0  
        pos = 1  
        s_ptr = 1 
        count = 0  
        
        while p < n and s_ptr < n:
            if s[p] == s[s_ptr]:
                p += 1
                s_ptr += 1
                count += 1
            else:
                p = 0
                pos += 1
                s_ptr = pos
                count = 0
        
        return count



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()

        ob = Solution()
        answer = ob.lps(s)
        print(answer)

# } Driver Code Ends