//{ Driver Code Starts
#include <bits/stdc++.h>

using namespace std;

// } Driver Code Ends
//User function template for C++
class Solution{
public:	

	int print2largest(int arr[], int n) {
	    // code here
	    int first = INT_MIN;
	    int second = INT_MIN;
	    
	    for (int i = 0; i < n; ++i) {
	        if (arr[i] > first) {
	            second = first; 
	            first = arr[i]; 
	        } else if (arr[i] > second && arr[i] != first) {
	            second = arr[i]; 
	        }
	    }
	    
	    return (second == INT_MIN) ? -1 : second;
	}
};


//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        int arr[n];
        for (int i = 0; i < n; i++) {
            cin >> arr[i];
        }
        Solution ob;
        auto ans = ob.print2largest(arr, n);
        cout << ans << "\n";
    }
    return 0;
}

// } Driver Code Ends