//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution {
  public:
    // Function to reverse words in a given string.
    string reverseWords(string str) {
        // code here
        vector<string> s;
        string word = "";
    
        for (int i = 0; i < str.size(); i++) {
            if (str[i] != '.') {
                word += str[i];  
            } 
            if (str[i] == '.' || i == str.size() - 1) {  
                if (str[i] == '.') {  
                    s.push_back(word);
                    word = "";  
                } 
                if (i == str.size() - 1) {  
                    s.push_back(word);
                }
            }
        }
        
        string ans = "";
        for (int i = s.size() - 1; i >= 0; i--) {
            ans += s[i];  
            if (i != 0) {
                ans += '.';  
            }
        }
        
        return ans;
    }
};




//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        string s;
        cin >> s;
        Solution obj;
        cout << obj.reverseWords(s) << endl;
    }
}
// } Driver Code Ends