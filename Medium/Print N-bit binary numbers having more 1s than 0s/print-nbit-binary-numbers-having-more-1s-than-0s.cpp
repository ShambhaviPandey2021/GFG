//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
//User function template for C++
class Solution{
public:	

    vector<string> result;
    
    void generate_binary(string number, int ones, int zeros, int n) {
        if (number.size() == n) {
            result.push_back(number);
            return;
        }

        if (ones >= zeros) {
            generate_binary(number + '1', ones + 1, zeros, n);
        }

        if (ones > zeros) {
            generate_binary(number + '0', ones, zeros + 1, n);
        }
    }
    
    vector<string> NBitBinary(int n) {
        generate_binary("", 0, 0, n);
        return result;
    }
};



//{ Driver Code Starts.

int main() 
{
   	

   	ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    cout.tie(NULL);
   
   	int t;
   	cin >> t;
   	while(t--)
   	{
   		int n;
   		cin >> n;
        Solution ob;
   		vector<string> ans = ob.NBitBinary(n);

   		for(auto i:ans)
   			cout << i << " ";

   		cout << "\n";
   	}

    return 0;
}
// } Driver Code Ends