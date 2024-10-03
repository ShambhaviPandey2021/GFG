//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution {
  public:
    // Function to find the majority elements in the array
    vector<int> findMajority(vector<int>& nums) {
        // Your code goes here.
        int ele1=nums[0],ele2=nums[0];
        int count1=0,count2=0;
        int n=nums.size();
        for(int i=0;i<n;i++){
            if(ele1==nums[i]) count1++;
            else if(ele2==nums[i]) count2++;
            else if(count1==0){
                ele1=nums[i];
                count1=1;
            }
            else if(count2==0){
                ele2=nums[i];
                count2=1;
            }
            else{
                count1--;
                count2--;
            }
        }
    
    int freq1=0,freq2=0;
    vector<int>ans;
    for(int i=0;i<n;i++){
        if(nums[i]==ele1) freq1++;
        else if (nums[i]==ele2)freq2++;
    }
    if(freq1>n/3) ans.push_back(ele1);
    if(freq2>n/3) ans.push_back(ele2);
    if(ans.size()==0) return {-1};
    return ans;
    }
};


//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    cin.ignore();
    while (t--) {

        string s;
        getline(cin, s);
        stringstream ss(s);
        vector<int> nums;
        int num;
        while (ss >> num) {
            nums.push_back(num);
        }
        Solution ob;
        vector<int> ans = ob.findMajority(nums);
        for (auto &i : ans)
            cout << i << " ";
        cout << "\n";
    }
    return 0;
}
// } Driver Code Ends