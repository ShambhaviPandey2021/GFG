//{ Driver Code Starts
// Initial template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function template for C++
class Solution {
public:
    vector<int> printKClosest(vector<int> arr, int n, int k,
                              int x)
    {
        // code here
        priority_queue<pair<int, int> > maxH;

        for (int i = 0; i < n; i++) {
      
            if (arr[i] == x)
                continue;
            maxH.push({ abs(arr[i] - x), -arr[i] });

            if (maxH.size() > k)
                maxH.pop();
        }

        vector<int> result;
        while (!maxH.empty()) {
            auto p = maxH.top();
            maxH.pop();
            result.push_back(-p.second);
        }

        reverse(result.begin(), result.end());

        return result;
    }
};


//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, k, x;
        cin >> n;
        vector<int> arr(n);
        for (int i = 0; i < n; i++) {
            cin >> arr[i];
        }
        cin >> k >> x;
        Solution ob;
        auto ans = ob.printKClosest(arr, n, k, x);
        for (auto e : ans) {
            cout << e << " ";
        }
        cout << "\n";
    }
    return 0;
}

// } Driver Code Ends