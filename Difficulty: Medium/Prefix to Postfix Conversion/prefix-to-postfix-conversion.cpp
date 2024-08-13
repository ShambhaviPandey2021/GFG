//{ Driver Code Starts
// Initial Template for C++
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function Template for C++

class Solution {
  public:
    string preToPost(string s) {
        stack<string> st;
        int n = s.size();
        
        for (int i = n - 1; i >= 0; i--) {
           
            if (isalpha(s[i]) || isdigit(s[i])) {
                st.push(string(1, s[i]));
            } else {
                
                string op1 = st.top();
                st.pop();
                string op2 = st.top();
                st.pop();
                string ans = op1 + op2 + s[i];
                st.push(ans);
            }
        }
        
        return st.top();

    }
};

//{ Driver Code Starts.

int main() {
    int t = 1;
    cin >> t;

    // freopen ("output_gfg.txt", "w", stdout);

    while (t--) {
        // Input
        string prefix;
        cin >> prefix;

        Solution obj;
        cout << obj.preToPost(prefix) << endl;

        // cout << "~\n";
    }
    // fclose(stdout);

    return 0;
}

// } Driver Code Ends