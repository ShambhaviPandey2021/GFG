//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++

#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int largestSubsquare(int n, vector<vector<char>>& a) {
        vector<vector<int>> row_matrix(n, vector<int>(n, 0));
        vector<vector<int>> col_matrix(n, vector<int>(n, 0));
        

        for (int i = 0; i < n; i++) {
            int row = 0;
            for (int j = 0; j < n; j++) {
                if (a[i][j] == 'X') {
                    row++;
                } else {
                    row = 0;
                }
                row_matrix[i][j] = row;
            }
        }

        for (int i = 0; i < n; i++) {
            int col = 0;
            for (int j = 0; j < n; j++) {
                if (a[j][i] == 'X') {
                    col++;
                } else {
                    col = 0;
                }
                col_matrix[j][i] = col;
            }
        }
        
        int result = 0;
    
        for (int i = n - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                int side = min(row_matrix[i][j], col_matrix[i][j]);
                while (side > result) {
                    if (row_matrix[i - side + 1][j] >= side && col_matrix[i][j - side + 1] >= side) {
                        result = side;
                        break;
                    } else {
                        side--;
                    }
                }
            }
        }
        
        return result;
    }
};


//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<vector<char>> a(n, vector<char>(n));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) cin >> a[i][j];
        }
        Solution ob;
        cout << ob.largestSubsquare(n, a) << "\n";
    }
}
// } Driver Code Ends