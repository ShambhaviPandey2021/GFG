
class Solution:
    def countDistinct(self, arr, k):
        # Code here
        n = len(arr)
        if k > n:
            return [] 

        freq = {}
        result = []
        for i in range(k):
            freq[arr[i]] = freq.get(arr[i], 0) + 1

        result.append(len(freq))

        for i in range(k, n):
            outgoing = arr[i - k]
            freq[outgoing] -= 1
            if freq[outgoing] == 0:
                del freq[outgoing]

            incoming = arr[i]
            freq[incoming] = freq.get(incoming, 0) + 1
            result.append(len(freq))

        return result


#{ 
 # Driver Code Starts
import sys
from collections import defaultdict
if __name__ == '__main__':
    input = sys.stdin.read
    data = input().splitlines()
    t = int(data[0])
    index = 1
    while t > 0:
        arr = list(map(int, data[index].strip().split()))
        index += 1
        k = int(data[index])
        index += 1

        ob = Solution()
        res = ob.countDistinct(arr, k)

        for element in res:
            print(element, end=" ")
        print()
        print("~")

        t -= 1

# } Driver Code Ends