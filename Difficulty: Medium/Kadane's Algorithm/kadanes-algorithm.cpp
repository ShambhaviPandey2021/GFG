//{ Driver Code Starts
// Initial Template for C++
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function Template for C++
class Solution {
  public:
    // Function to find the sum of contiguous subarray with maximum sum.
    int maxSubarraySum(vector<int> &arr) {
        // code here...
        int maxi = INT_MIN;
        int sum = 0;
        int ans= -1;
        int start =0;
        int ansEnd = -1;
        for(int i = 0;i<arr.size();i++){
            if(sum==0){
                start = i;
            }
            sum = sum + arr[i];
            if(sum>maxi){
                maxi = sum;
                ans = start;
                ansEnd = i;
            }
            if(sum<0){
                sum = 0;
            }
        }
        return maxi;
    }
};


//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    cin.ignore(); // To discard any leftover newline characters
    while (t--)   // while testcases exist
    {
        vector<int> arr;
        string input;
        getline(cin, input); // Read the entire line for the array elements
        stringstream ss(input);
        int number;
        while (ss >> number) {
            arr.push_back(number);
        }

        Solution ob;
        cout << ob.maxSubarraySum(arr) << endl;
    }
}
// } Driver Code Ends