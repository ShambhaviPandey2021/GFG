//{ Driver Code Starts

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution {
  public:
    string binaryNextNumber(string s) {
        // code here.
        reverse(s.begin(), s.end());
        int carry=1;
        for(int i=0;i<s.length() && carry==1;i++){
            if(s[i]=='0'){
                s[i]='1';
                carry=0;
            }
            else{
                s[i]='0';
                carry=1;
            }
        }
        if(carry){
            s=s+'1';
        }
        reverse(s.begin(), s.end());
        int idx=0;
        while(s[idx]=='0'){
            idx++;
        }
        int n=s.length();
        return s.substr(idx,n-idx);
    }
};


//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        string s;
        cin >> s;
        Solution ob;
        cout << ob.binaryNextNumber(s);
        cout << "\n";
    }

    return 0;
}
// } Driver Code Ends