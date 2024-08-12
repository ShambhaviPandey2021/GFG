#User function Template for python3

class Solution:
    def sum_of_middle_elements(self, arr1, arr2):
        n = len(arr1)
        i, j = 0, 0
        m1, m2 = -1, -1

        count = 0
        while count < n + 1:
            if i == n:
                m1 = m2
                m2 = arr2[j]
                break
            elif j == n:
                m1 = m2
                m2 = arr1[i]
                break

            if arr1[i] <= arr2[j]:
                m1 = m2
                m2 = arr1[i]
                i += 1
            else:
                m1 = m2
                m2 = arr2[j]
                j += 1

            count += 1

        return m1 + m2

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

input = sys.stdin.read


def main():
    input_lines = input().strip().split("\n")
    t = int(input_lines[0])

    index = 1
    results = []
    while t > 0:
        arr = list(map(int, input_lines[index].strip().split()))
        brr = list(map(int, input_lines[index + 1].strip().split()))
        index += 2

        solution = Solution()
        res = solution.sum_of_middle_elements(arr, brr)
        results.append(res)

        t -= 1

    for result in results:
        print(result)


if __name__ == "__main__":
    main()

# } Driver Code Ends