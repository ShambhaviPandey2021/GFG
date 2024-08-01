//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution {
  public:
    vector<int> spirallyTraverse(vector<vector<int> > &matrix) {
        // code here
        int row=matrix.size();
        int col=matrix[0].size();

        int top = 0 , bottom = row - 1  ,left = 0  , right = col - 1 ;
        vector<int> result;

        while (left <= right && top <= bottom) {
            //print top row
            for(int i = left;i<=right;i++){
               result.push_back(matrix[top][i]);
            }
            top++;
            
            //print right column
            for(int i = top;i<=bottom;i++){
                result.push_back(matrix[i][right]);
            }
            right--;
            
            
            if(top<=bottom){
                for(int i = right;i>=left;i--){
                    result.push_back(matrix[bottom][i]);
                }
                bottom--;
                    
            }
            
            if(left<=right){
                for(int i = bottom;i>=top;i--){
                    result.push_back(matrix[i][left]);
                }
                left++;
                    
            }
        }
        return result;
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;

    while (t--) {
        int r, c;
        cin >> r >> c;
        vector<vector<int>> matrix(r, vector<int>(c, 0));

        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                cin >> matrix[i][j];
            }
        }

        Solution ob;
        vector<int> result = ob.spirallyTraverse(matrix);
        for (int i = 0; i < result.size(); ++i)
            cout << result[i] << " ";
        cout << endl;
    }
    return 0;
}
// } Driver Code Ends