//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution{
    public:
    int lenOfLongSubarr(int A[], int N, int K) { 
        unordered_map<int, int> preSumMap;
        int maxLen = 0;
        int sum = 0;
        
        for (int i = 0; i < N; i++) {
            sum += A[i];
            
            // Check if the sum is equal to the target sum K
            if (sum == K) {
                maxLen = i + 1;
            }
            
            // Calculate the remaining sum to find in the map
            int rem = sum - K;
            
            // Check if the remaining sum exists in the map
            if (preSumMap.find(rem) != preSumMap.end()) {
                int len = i - preSumMap[rem];
                maxLen = max(maxLen, len);
            }
            
            // Insert the current sum with its index if it's not already present
            if (preSumMap.find(sum) == preSumMap.end()) {
                preSumMap[sum] = i;
            }
        }
        return maxLen;
    }
};


//{ Driver Code Starts.

int main() {
	//code
	
	int t;cin>>t;
	while(t--)
	{
	    int n, k;
	    cin>> n >> k;
	    int a[n];
	    
	    for(int i=0;i<n;i++)
	        cin>>a[i];
	   Solution ob;
	   cout << ob.lenOfLongSubarr(a, n , k)<< endl;
	    
	}
	
	return 0;
}
// } Driver Code Ends