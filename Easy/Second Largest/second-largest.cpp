//{ Driver Code Starts
#include <bits/stdc++.h>

using namespace std;

// } Driver Code Ends
//User function template for C++
class Solution{
public:	
	// Function returns the second
	// largest elements
    int print2largest(int arr[], int n) {
        int maxElement = INT_MIN;
        int secondMaxElement = INT_MIN;
        for(int i = 0; i< n ; i++){
            if(arr[i] > maxElement){
                secondMaxElement = maxElement;
                maxElement = arr[i];
            } else if(arr[i] != maxElement && arr[i] > secondMaxElement){
                secondMaxElement = arr[i];
            }
        }
        return secondMaxElement != INT_MIN ? secondMaxElement : -1;
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