//{ Driver Code Starts
// Initial Template for C++
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function Template for C++

class Solution {
  public:
    string preToInfix(string s) {
        // Write your code here
        stack<string>st;
        string ans;
        int n = s.size();
        for(int i = n-1; i>=0;i--){
            
            if(isalpha(s[i]) || isdigit(s[i])){
                st.push(string(1,s[i]));

            }
            else{
                string top1 = st.top();
                st.pop();
                string top2 = st.top();
                st.pop();
                string ans = "("+ top1 + s[i] + top2 + ")";
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
        cout << obj.preToInfix(prefix) << endl;

        // cout << "~\n";
    }
    // fclose(stdout);

    return 0;
}

// } Driver Code Ends