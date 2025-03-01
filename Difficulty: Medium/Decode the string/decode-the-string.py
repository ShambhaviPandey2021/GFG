
class Solution:
    def decodedString(self, s):
        # code here
        stack = []
        for char in s:
            if char != "]":
                stack.append(char)
            else:
                encoded_str = ""
                while stack and stack[-1] != "[":
                    encoded_str = stack.pop() + encoded_str
                stack.pop()
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                repeat_cnt = int(num)

                stack.append(encoded_str * repeat_cnt)
        return "".join(stack)
            
            
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()

        ob = Solution()
        print(ob.decodedString(s))
        print("~")

# } Driver Code Ends