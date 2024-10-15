//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution {
  public:
    // Function to count the number of subarrays which adds to the given sum.
    int subArraySum(vector<int>& arr, int tar) {
        // Your code here
        unordered_map<int, int> prefixSumCount;
        int prefix_sum = 0;
        int count = 0;
        
        for (int num : arr) {
           
            prefix_sum += num;
            
            if (prefix_sum == tar) {
                count++;
            }
            
            if (prefixSumCount.find(prefix_sum - tar) != prefixSumCount.end()) {
                count += prefixSumCount[prefix_sum - tar];
            }
            
            prefixSumCount[prefix_sum]++;
        }
        
        return count;

    }
};

//{ Driver Code Starts.

int main() {
    string ts;
    getline(cin, ts);
    int t = stoi(ts);
    while (t--) {

        vector<int> arr;
        string input;
        getline(cin, input);
        stringstream ss(input);
        int number;
        while (ss >> number) {
            arr.push_back(number);
        }
        string ks;
        getline(cin, ks);
        int tar = stoi(ks);
        Solution obj;
        int res = obj.subArraySum(arr, tar);
        cout << res << endl;
    }
    return 0;
}
// } Driver Code Ends