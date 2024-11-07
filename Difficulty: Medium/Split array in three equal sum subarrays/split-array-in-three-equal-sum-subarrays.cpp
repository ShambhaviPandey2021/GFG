//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function Template for C++
//  Class Solution to contain the method for solving the problem.
class Solution {
  public:
    // Function to determine if array arr can be split into three equal sum sets.
    vector<int> findSplit(vector<int>& arr) {
        // code here
        int n = arr.size();
        int totalSum = accumulate(arr.begin(), arr.end(), 0);
        
        if (totalSum % 3 != 0) return {-1, -1};
        
        int target = totalSum / 3;
        int currentSum = 0;
        int firstSplit = -1, secondSplit = -1;
        
        for (int i = 0; i < n; ++i) {
            currentSum += arr[i];
            
            if (currentSum == target && firstSplit == -1) {
                firstSplit = i;
            }
            else if (currentSum == 2 * target && firstSplit != -1) {
                secondSplit = i;
                break;
            }
        }
        
        if (firstSplit != -1 && secondSplit != -1) {
            return {firstSplit, secondSplit};
        }
        
        return {-1, -1};
    }
};


//{ Driver Code Starts.

int main() {
    int test_cases;
    cin >> test_cases;
    cin.ignore();
    while (test_cases--) {
        string input;
        vector<int> arr;

        // Read the array from input line
        getline(cin, input);
        stringstream ss(input);
        int number;
        while (ss >> number) {
            arr.push_back(number);
        }

        // Solution instance to invoke the function
        Solution ob;
        vector<int> result = ob.findSplit(arr);

        // Output result
        if (result[0] == -1 && result[1] == -1) {
            cout << "false" << endl;
        } else {
            cout << "true" << endl;
        }
    }
    return 0;
}

// } Driver Code Ends