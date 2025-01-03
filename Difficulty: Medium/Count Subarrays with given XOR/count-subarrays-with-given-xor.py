class Solution:
    def subarrayXor(self, arr, k):
        # code here
        count = 0
        curr_xor= 0
        freq = {0: 1}  
        
        for num in arr:
            curr_xor ^= num
            if curr_xor ^ k in freq:
                count += freq[curr_xor ^ k]
            freq[curr_xor] = freq.get(curr_xor, 0) + 1
        
        return count


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    tc = int(input())

    for _ in range(tc):
        arr = list(map(int, input().split()))
        k = int(input())

        obj = Solution()
        print(obj.subarrayXor(arr, k))
        print("~")

# } Driver Code Ends