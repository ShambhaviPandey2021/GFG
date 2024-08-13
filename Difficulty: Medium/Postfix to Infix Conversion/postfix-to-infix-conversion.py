#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def postToInfix(self, s):
        # Code here
        stack = []
        n = len(s)
        for i in range(n):
            if s[i].isalpha() or s[i].isdigit():
                stack.append(s[i])
            else:
                op1 = stack.pop()
                op2 = stack.pop()
                ans = '(' + op2 + s[i] + op1 + ')'
                stack.append(ans)
        return stack[-1]
        

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        postfix = input()
        ob = Solution()
        res = ob.postToInfix(postfix)
        print(res)
# } Driver Code Ends