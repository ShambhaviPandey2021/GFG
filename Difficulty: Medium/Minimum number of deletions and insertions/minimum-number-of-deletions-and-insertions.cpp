//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends

class Solution{
	public:
    int lcs(const string& str1, int n, const string& str2, int m, vector<vector<int>>& dp) {
  
        if (n == 0 || m == 0) {
            return 0;
        }

        if (dp[n][m] != -1) {
            return dp[n][m];
        }

        if (str1[n - 1] == str2[m - 1]) { 
            return dp[n][m] = 1 + lcs(str1, n - 1, str2, m - 1, dp);
        }

        return dp[n][m] = max(lcs(str1, n - 1, str2, m, dp), lcs(str1, n, str2, m - 1, dp));
    }

    int minOperations(const string& str1, const string& str2) {
        int n = str1.length();
        int m = str2.length();
        vector<vector<int>> dp(n + 1, vector<int>(m + 1, -1)); 
        int lcsLen = lcs(str1, n, str2, m, dp); 
      

        return (n - lcsLen) + (m - lcsLen);
    }
};




//{ Driver Code Starts.
int main() 
{
   	
   
   	int t;
    cin >> t;
    while (t--)
    {
        string s1, s2;
        cin >> s1 >> s2;

	    Solution ob;
	    cout << ob.minOperations(s1, s2) << "\n";
	     
    }
    return 0;
}


// } Driver Code Ends