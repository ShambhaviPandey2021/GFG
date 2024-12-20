class Solution:
    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, mat):
        # code here
        n = len(mat)
        m = len(mat[0])
        top, left = 0, 0
        bottom, right = n - 1, m - 1
        result = []

        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                result.append(mat[top][i])
            top += 1
            for i in range(top, bottom + 1):
                result.append(mat[i][right])
            right -= 1

            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(mat[bottom][i])
                bottom -= 1

            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(mat[i][left])
                left += 1

        return result


#{ 
 # Driver Code Starts
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

        solution = Solution()
        result = solution.spirallyTraverse(matrix)
        print(" ".join(map(str, result)))
        print("~")

# } Driver Code Ends