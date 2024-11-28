#User function template for Python
class Solution:
    def myAtoi(self, s):
        # Code here
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        s = s.strip()
        if not s:
            return 0 

        sign = 1  
        i = 0 
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1

        result = 0
        while i < len(s) and s[i].isdigit():
            result = result * 10 + int(s[i])

            if result * sign > INT_MAX:
                return INT_MAX
            if result * sign < INT_MIN:
                return INT_MIN

            i += 1

        return result * sign




#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        ob = Solution()
        print(ob.myAtoi(s))
        print("~")

# } Driver Code Ends