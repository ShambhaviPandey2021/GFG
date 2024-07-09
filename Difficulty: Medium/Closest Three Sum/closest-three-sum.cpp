//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function template for C++

// arr : given vector of elements
// target : given sum value

class Solution {
  public:
    int threeSumClosest(vector<int> arr, int target) {
    

        int n = arr.size();
        sort(arr.begin(), arr.end());
        int ans = 0;
        int diff=INT_MAX;// Initialize with the first three elements
        
        for (int i = 0; i < n - 2; ++i) {
            int left = i + 1, right = n - 1;
            while (left < right) {
                int sum = arr[i] + arr[left] + arr[right];
                int d = abs(sum-target);
                if(d<diff){
                    diff=d;
                    ans=sum;
                }
                else if(d==diff){
                    ans = max(ans,sum);
                }
                if(sum<target){
                    left++;
                }
                else if(sum==target){
                    return sum;
                }
                else{
                    right--;
                }
                
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
        cin.ignore();
        vector<int> arr;
        string input;
        getline(cin, input);
        stringstream ss(input);
        int number;
        while (ss >> number) {
            arr.push_back(number);
        }
        int key;
        cin >> key;
        // cin.ignore();
        // if (f)
        //     return 0;
        Solution ob;
        cout << ob.threeSumClosest(arr, key) << endl;
    }
    return 0;
}
// } Driver Code Ends