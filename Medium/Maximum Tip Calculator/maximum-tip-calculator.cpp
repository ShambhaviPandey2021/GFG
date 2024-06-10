//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

class Array {
  public:
    template <class T>
    static void input(vector<T> &a, int n) {
        for (int i = 0; i < n; i++) {
            scanf("%d ", &a[i]);
        }
    }

    template <class T>
    static void print(vector<T> &a) {
        for (int i = 0; i < a.size(); i++) {
            cout << a[i] << " ";
        }
        cout << endl;
    }
};


// } Driver Code Ends

class Solution {
  public:
    long long maxTip(int n, int x, int y, vector<int> &arr, vector<int> &brr) {
        // code here
        vector<pair<int, int>> differences(n);
        for (int i = 0; i < n; ++i) {
            differences[i] = {abs(arr[i] - brr[i]), i};
        }

        // Sort the orders by the absolute difference in descending order
        sort(differences.rbegin(), differences.rend());

        long long totalTip = 0;
        int countA = 0, countB = 0;

        for (int i = 0; i < n; ++i) {
            int index = differences[i].second;

            // If waiter A has not reached the limit and either:
            // - waiter B has reached the limit or
            // - the tip for waiter A is greater than or equal to the tip for waiter B
            if ((countA < x && arr[index] >= brr[index]) || countB >= y) {
                totalTip += arr[index];
                countA++;
            } else {
                totalTip += brr[index];
                countB++;
            }
        }

        return totalTip;
    }
};


//{ Driver Code Starts.

int main() {
    int t;
    scanf("%d ", &t);
    while (t--) {

        int n;
        scanf("%d", &n);

        int x;
        scanf("%d", &x);

        int y;
        scanf("%d", &y);

        vector<int> arr(n);
        Array::input(arr, n);

        vector<int> brr(n);
        Array::input(brr, n);

        Solution obj;
        long long res = obj.maxTip(n, x, y, arr, brr);

        cout << res << endl;
    }
}

// } Driver Code Ends