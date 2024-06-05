//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution {

  public:
    int findSwapValues(int a[], int n, int b[], int m) {
        // Your code goes here
        int sum_a = 0;
        int sum_b = 0;
        for(int i =0;i<n;i++){
            sum_a += a[i];
        }
        for(int i =0;i<m;i++){
            sum_b += b[i];
        }
        if((sum_a - sum_b)%2!=0){
            return -1;
        }
        int target = (sum_a - sum_b)/2;
        sort(a,a+n);
        sort(b,b+m);
        
        int i = 0 , j = 0 ;
        while(i<n && j<m){
            int diff = a[i] - b[j];
            if(diff==target){
                return 1;
            }
            else if(diff<target){
                i++;
            }
            else{
                j++;
            }
        }
        return -1;
    }
};

//{ Driver Code Starts.

int main() {

    int t;
    cin >> t;
    while (t--) {
        int n, m;
        cin >> n >> m;
        int a[n];
        int b[m];
        for (int i = 0; i < n; i++)
            cin >> a[i];
        for (int i = 0; i < m; i++)
            cin >> b[i];

        Solution ob;
        cout << ob.findSwapValues(a, n, b, m);
        cout << "\n";
    }
    return 0;
}

// } Driver Code Ends