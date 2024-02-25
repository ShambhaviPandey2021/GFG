#User function Template for python3

from collections import Counter

def isSubset(a1, a2, n, m):
    count_a1 = Counter(a1)
    count_a2 = Counter(a2)
    
    for num, count in count_a2.items():
        if count_a1[num] < count:
            return "No"
    return "Yes"



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m = sz[0], sz[1]
        a1 = [int(x) for x in input().strip().split()]
        a2 = [int(x) for x in input().strip().split()]
        
        print(isSubset( a1, a2, n, m))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends