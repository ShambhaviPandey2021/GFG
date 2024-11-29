#User function Template for python3
class Solution:
	def addBinary(self, s1, s2):
		# code here
        ans = ""
        i, j = len(s1) - 1, len(s2) - 1
        carry = 0
        while i >= 0 or j >= 0:
            count1s = 0
            if i >= 0 and s1[i] == '1':
                count1s += 1
            if j >= 0 and s2[j] == '1':
                count1s += 1

            if count1s + carry == 0:
                ans += '0'
                carry = 0
            elif count1s + carry == 1:
                ans += '1'
                carry = 0
            elif count1s + carry == 2:
                ans += '0'
                carry = 1
            elif count1s + carry == 3:
                ans += '1'
                carry = 1

            i -= 1
            j -= 1
        if carry == 1:
            ans += '1'

        ans = ans[::-1]
        ans = ans.lstrip('0')

        return ans if ans else "0"




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        a = input().strip()
        b = input().strip()
        ob = Solution()
        answer = ob.addBinary(a, b)

        print(answer)
        print("~")

# } Driver Code Ends