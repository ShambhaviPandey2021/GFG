//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution {
  public:
    // Function to return the minimum cost of connecting the ropes.
    long long minCost(vector<long long>& arr) {
        // Your code here
        priority_queue<long long, vector<long long>,greater<long long>> min_h;
        for(long long num:arr){
            min_h.push(num);
        }
        long long cost = 0;
        while(min_h.size()>1){
            long long first = min_h.top();
            min_h.pop();
            long long sec = min_h.top();
            min_h.pop();
            long long comb = first + sec;
            cost += comb;
            min_h.push(comb);
        }
        return cost;
    }
};


//{ Driver Code Starts.

int main() {
    long long t;
    cin >> t;
    cin.ignore();
    while (t--) {
        string input;
        long long num;
        vector<long long> a;

        getline(cin, input);
        stringstream s2(input);
        while (s2 >> num) {
            a.push_back(num);
        }
        Solution ob;
        cout << ob.minCost(a) << endl;
    }
    return 0;
}

// } Driver Code Ends