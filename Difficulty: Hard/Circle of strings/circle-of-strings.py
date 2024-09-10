#User function Template for python3


from collections import defaultdict, deque

class Solution:
    def isCircle(self, arr):

        graph = defaultdict(list)
        in_degree = defaultdict(int)
        out_degree = defaultdict(int)
      
        for word in arr:
            first_char = word[0]
            last_char = word[-1]
            graph[first_char].append(last_char)
            out_degree[first_char] += 1
            in_degree[last_char] += 1
        
        all_chars = set(out_degree.keys()).union(set(in_degree.keys()))
        
        for char in all_chars:
            if in_degree[char] != out_degree[char]:
                return 0  
        
        def dfs(v, visited):
            visited.add(v)
            for neighbor in graph[v]:
                if neighbor not in visited:
                    dfs(neighbor, visited)
        
        start_char = arr[0][0]
        visited = set()
        dfs(start_char, visited)
        
        if visited != all_chars:
            return 0  
        
        return 1  


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

sys.setrecursionlimit(10**6)
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        A = input().split()

        ob = Solution()
        print(ob.isCircle(A))

# } Driver Code Ends